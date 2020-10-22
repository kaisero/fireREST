# -*- coding: utf-8 -*-

import json
import logging
import requests
import urllib3

from . import defaults
from . import exceptions as exc
from . import utils

from copy import deepcopy
from http.client import responses as http_responses
from packaging import version
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError
from time import sleep
from typing import Dict, List
from urllib.parse import urlencode
from uuid import UUID

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Client(object):
    def __init__(
        self,
        hostname: str,
        username: str,
        password: str,
        protocol=defaults.API_PROTOCOL,
        verify_cert=False,
        cache=False,
        domain=defaults.API_DEFAULT_DOMAIN,
        timeout=defaults.API_REQUEST_TIMEOUT,
    ):
        '''
        Initialize api client object (make sure to use a dedicated api user!)
        :param hostname: ip address or dns name of fmc
        :param username: fmc username
        :param password: fmc password
        :param protocol: protocol used to access fmc rest api
        :param verify_cert: check https certificate for validity
        :param cache: enable result caching for get operations
        :param logger: optional logger instance
        :param domain: name of the domain to access
        :param timeout: timeout value for http requests
        '''
        if not verify_cert:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers = {
            'Content-Type': defaults.API_CONTENT_TYPE,
            'Accept': defaults.API_CONTENT_TYPE,
            'User-Agent': defaults.API_USER_AGENT,
        }
        self.cache = cache
        self.cred = HTTPBasicAuth(username, password)
        self.hostname = hostname
        self.protocol = protocol
        self.refresh_counter = defaults.API_REFRESH_COUNTER_INIT
        self.session = requests.Session()
        self.timeout = timeout
        self.verify_cert = verify_cert
        self._login()
        self.domain_name = domain
        self.domain = self.get_domain_id(domain)
        self.version = version.parse(self.get_system_version()[0]['serverVersion'].split(' ')[0])

    def _url(self, namespace='base', path=''):
        '''
        Generate url on the for requests to fmc rest api
        : param namespace: name of the url namespace that should be used. options: base, config, auth. default = base
        : param path: the url path for which a full url should be created
        : return: url in string format
        '''
        options = {
            'base': f'{self.protocol}://{self.hostname}{path}',
            'config': f'{self.protocol}://{self.hostname}{defaults.API_CONFIG_URL}/domain/{self.domain}{path}',
            'platform': f'{self.protocol}://{self.hostname}{defaults.API_PLATFORM_URL}{path}',
            'refresh': f'{self.protocol}://{self.hostname}{defaults.API_REFRESH_URL}',
        }
        if namespace not in options.keys():
            raise exc.InvalidNamespaceError(f'Invalid namespace "{namespace}" provided. Options: {options.keys()}')
        return options[namespace].rstrip('/')

    def _virtualrouter_url(self, url, virtualrouter_id=''):
        '''
        Change url to include path to virtualrouter
        : param virtualrouter_id: uuid of virtualrouter
        : return: adapted url that points to specified virtualrouter, same url if no virtualrouter is specified
        '''
        if virtualrouter_id:
            return url.replace('/routing/', f'/routing/virtualrouters/{virtualrouter_id}/')
        return url

    def _filter(self, items=None):
        '''
        Get filter string from list of key, value pairs
        : param items: list of key value pairs used to build filter string
        : return: valid filter string
        '''
        if items:
            filter_str = ''
            for k, v in items.items():
                if v:
                    filter_str += f'{k}:{v};'
            return filter_str.rstrip(';')
        return ''

    @utils.handle_errors
    def _request(self, method: str, url: str, params=None, auth=None, data=None):
        if params:
            logger.info('[%s] %s?%s', method.upper(), url, urlencode(params))
        else:
            logger.info('[%s] %s', method.upper(), url)
        if data:
            logger.debug(data)
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            data=json.dumps(data),
            auth=auth,
            headers=self.headers,
            timeout=self.timeout,
            verify=self.verify_cert,
        )
        logger.info('[RESPONSE] %s (%s)', http_responses[response.status_code], response.status_code)
        if response.text:
            if method == 'get':
                logger.debug('\n%s', json.dumps(response.json(), sort_keys=True, indent=4))
            else:
                logger.debug(response.text)
        return response

    def _get(self, url: str, params=None, items=None):
        '''
        GET operation with paging support
        : param url: request that should be performed
        : param params: dict of parameters for http request
        : return: dictionary or list containing api objects
        '''
        if not utils.is_getbyid_operation(url) and items is None:
            if params is None:
                params = {}
            params['limit'] = defaults.API_PAGING_LIMIT
            params['expanded'] = defaults.API_EXPANSION_MODE

        response = self._request('get', url, params=params)
        payload = response.json()

        if 'paging' in payload:
            if items is None:
                items = []
            if 'items' in payload:
                items.extend(payload['items'])
                if 'next' in payload['paging']:
                    items = self._get(payload['paging']['next'][0], params=None, items=items)
            return items
        return payload

    def _login(self):
        '''
        Login to fmc rest api
        '''
        logger.info('Attempting authentication with Firepower Management Center (%s)', self.hostname)
        url = f'{self.protocol}://{self.hostname}{defaults.API_AUTH_URL}'
        response = self._request('post', url, auth=self.cred)
        self.headers['X-auth-access-token'] = response.headers['X-auth-access-token']
        self.headers['X-auth-refresh-token'] = response.headers['X-auth-refresh-token']
        self.domains = json.loads(response.headers['DOMAINS'])
        self.refresh_counter = defaults.API_REFRESH_COUNTER_INIT

    def _refresh(self):
        '''
        Refresh authorization token. This operation is performed for up to three
        times, afterwards a re-authentication using _login() will be performed
        '''
        if self.refresh_counter < defaults.API_REFRESH_COUNTER_MAX:
            logger.info('Access token is invalid. Refreshing authentication token')
            url = self._url('refresh')
            response = self._request('post', url)
            self.headers['X-auth-access-token'] = response.headers['X-auth-access-token']
            self.headers['X-auth-refresh-token'] = response.headers['X-auth-refresh-token']
            self.refresh_counter += 1
        else:
            logger.info('Maximum number of authentication refresh operations reached', self.hostname)
            self._login()

    def _delete(self, url: str, params=None):
        '''
        DELETE operation
        : param url: request that should be performed
        : param params: dict of parameters for http request
        : return: requests.Response object
        '''
        return self._request('delete', url, params=params)

    def _post(self, url: str, data: Dict, params=None):
        '''
        CREATE operation
        : param url: request that should be performed
        : param json: dictionary of data that will be sent to the api
        : param params: dict of parameters for http request
        : return: requests.Response object
        '''
        data = self._sanitize('post', data)
        return self._request('post', url, params=params, data=data)

    def _put(self, url: str, data: Dict, params=None):
        '''
        UPDATE operation
        : param url: request that should be performed
        : param json: dictionary of data that will be sent to the api
        : param params: dict of parameters for http request
        : return: requests.Response object
        '''
        data = self._sanitize('put', data)
        return self._request('put', url, data=data, params=params)

    def _sanitize(self, method: str, payload: Dict):
        '''
        Sanitize json object for api operation
        This is neccesarry since fmc api cannot handle json objects with some
        fields that are received from GET (e.g. link, metadata)
        : param payload: api object in json format
        : return: sanitized api object in json format
        '''
        sanitized_payload = deepcopy(payload)
        if not isinstance(payload, list):
            sanitized_payload.pop('metadata', None)
            sanitized_payload.pop('links', None)
            if method.lower() == 'post':
                sanitized_payload.pop('id', None)
        else:
            for item in sanitized_payload:
                item.pop('metadata', None)
                item.pop('links', None)
                if method.lower() == 'post':
                    item.pop('id', None)
        return sanitized_payload

    @utils.validate_object_type
    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_object_id(self, object_type: str, object_name: str):
        '''
        helper function to retrieve object id by name
        : param object_type: object type that will be queried
        : param object_name: name of the object
        : return: object id if object is found, None otherwise
        '''
        objects = self.get_objects(object_type)
        for obj in objects:
            if obj['name'] == object_name:
                return obj['id']
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_id(self, name: str):
        '''
        helper function to retrieve device id by name
        : param name: name of the device
        : return: device id if device is found, None otherwise
        '''
        devices = self.get_devices()
        for device in devices:
            if device['name'] == name:
                return device['id']
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_devicehapair_id(self, name: str):
        '''
        helper function to retrieve device ha - pair id by name
        : param name: name of the hapair
        : return: id if hapair is found, None otherwise
        '''
        devicehapairs = self.get_devicehapairs()
        for devicehapair in devicehapairs:
            if devicehapair['name'] == name:
                return devicehapair['id']
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_device_id_from_devicehapair(self, devicehapair_id: str):
        '''
        helper function to retrieve device id from hapair
        : param devicehapair_id: id of hapair
        : return: id if device is found, None otherwise
        '''
        devicehapair = self.get_devicehapair(devicehapair_id)
        return devicehapair['primary']['id']

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_natpolicy_id(self, name: str):
        '''
        helper function to retrieve nat policy id by name
        : param name: name of nat policy
        : return: policy id if nat policy is found, None otherwise
        '''
        policies = self.get_natpolicies()
        for policy in policies:
            if policy['name'] == name:
                return policy['id']
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_accesspolicy_id(self, name: str):
        '''
        helper function to retrieve access control policy id by name
        : param name: name of the access control policy
        : return: accesspolicy id if access control policy is found, None otherwise
        '''
        policies = self.get_accesspolicies()
        for policy in policies:
            if policy['name'] == name:
                return policy['id']
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_filepolicy_id(self, name: str):
        '''
        helper function to retrieve file policy id by name
        : param name: name of the file policy
        : return: policy id if file policy is found, None otherwise
        '''
        policies = self.get_filepolicies()
        for policy in policies:
            if policy['name'] == name:
                return policy['id']
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_intrusionpolicy_id(self, name: str):
        '''
        helper function to retrieve intrusion policy id by name
        : param name: name of the intrusion policy
        : return: policy id if intrusion policy is found, None otherwise
        '''
        policies = self.get_intrusionpolicies()
        for policy in policies:
            if policy['name'] == name:
                return policy['id']
        return None

    def get_prefilterpolicy_id(self, name: str):
        '''
        helper function to retrieve prefilter policy id by name
        : param name: name of the prefilter policy
        : return: prefilter policy id if policy name is found, None otherwise
        '''
        prefilterpolicies = self.get_prefilterpolicies()
        for policy in prefilterpolicies:
            if policy['name'] == name:
                return policy['id']
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_accesspolicy_rule_id(self, policy_id: str, rule_name: str):
        '''
        helper function to retrieve access control policy rule id by name
        : param policy_id: id of the accesspolicy that will be queried
        : param rule_name: name of the accessrule
        : return: accesspolicy rule id if accessrule is found, None otherwise
        '''
        request = f'/policy/accesspolicies/{policy_id}/accessrules'
        url = self._url(defaults.API_CONFIG_NAME, request)
        accessrules = self._get(url)
        for accessrule in accessrules:
            if accessrule['name'] == rule_name:
                return accessrule['id']
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_syslogalert_id(self, name: str):
        '''
        helper function to retrieve syslog alert object id by name
        : param name: name of syslog alert object
        : return: syslogalert id if syslog alert is found, None otherwise
        '''
        syslogalerts = self.get_syslogalerts()
        for syslogalert in syslogalerts:
            if syslogalert['name'] == name:
                return syslogalert['id']
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_snmpalert_id(self, name: str):
        '''
        helper function to retrieve snmp alert object id by name
        : param name: name of snmp alert object
        : return: snmpalert id if snmp alert is found, None otherwise
        '''
        snmpalerts = self.get_snmpalerts()
        for snmpalert in snmpalerts:
            if snmpalert['name'] == name:
                return snmpalert['id']
        return None

    def get_domain_id(self, domain_name: str):
        '''
        helper function to retrieve domain id from list of domains
        : param domain_name: name of the domain
        : return: did if domain is found, None otherwise
        '''
        for domain in self.domains:
            if domain['name'] == domain_name:
                return domain['uuid']
        logger.error(
            'Could not find domain with name %s. Make sure full path is provided', domain_name,
        )
        available_domains = ', '.join((domain['name'] for domain in self.domains))
        logger.debug('Available Domains: %s', available_domains)
        return None

    def get_domain_name_by_id(self, domain_id: str):
        '''
        helper function to retrieve domain name by id
        : param domain_id: id of the domain
        : return: name if domain is found, None otherwise
        '''
        for domain in self.domains:
            if domain['uuid'] == domain_id:
                return domain['name']
        logger.error(
            'Could not find domain with id %s. Make sure full path is provided', domain_id,
        )
        available_domains = ', '.join((domain['uuid'] for domain in self.domains))
        logger.debug('Available Domains: %s', available_domains)
        return None

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_system_version(self):
        url = self._url(defaults.API_PLATFORM_NAME, '/info/serverversion')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_audit_records(self):
        url = self._url(defaults.API_CONFIG_NAME, '/audit/auditrecords')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_audit_record(self, record_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/audit/auditrecords/{record_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_syslogalerts(self):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/syslogalerts')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_snmpalerts(self):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/snmpalerts')
        return self._get(url)

    @utils.validate_object_type
    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def create_object(self, object_type: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/object/{object_type}')
        return self._post(url, data)

    @utils.validate_object_type
    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_objects(self, object_type: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/object/{object_type}')
        return self._get(url)

    @utils.validate_object_type
    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_objects_overrides(self, object_type: str, objects: List):
        overrides = []
        for obj in objects:
            if obj['overridable']:
                overrides.extend(self.get_object_overrides(object_type, obj['id']))
        return overrides

    @utils.validate_object_type
    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_object(self, object_type: str, object_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/object/{object_type}/{object_id}')
        return self._get(url)

    @utils.validate_object_type
    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_object_overrides(self, object_type: str, object_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/object/{object_type}/{object_id}/overrides')
        return self._get(url)

    @utils.validate_object_type
    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_object(self, object_type: str, object_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/object/{object_type}/{object_id}')
        return self._put(url, data)

    @utils.validate_object_type
    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def delete_object(self, object_type: str, object_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/object/{object_type}/{object_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def create_devicegroup(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/devicegroups/devicegrouprecords')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_devicegroups(self):
        url = self._url(defaults.API_CONFIG_NAME, '/devicegroups/devicegrouprecords')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_devicegroup(self, devicegroup_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devicegroups/devicegrouprecords/{devicegroup_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_devicegroup(self, devicegroup_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devicegroups/devicegrouprecords/{devicegroup_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def delete_devicegroup(self, devicegroup_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devicegroups/devicegrouprecords/{devicegroup_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def create_device(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/devices/devicerecords')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_devices(self):
        url = self._url(defaults.API_CONFIG_NAME, '/devices/devicerecords')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_device(self, device_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def delete_device(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_devicehapairs(self):
        url = self._url(defaults.API_CONFIG_NAME, '/devicehapairs/ftddevicehapairs')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def create_devicehapair(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/devicehapairs/ftddevicehapairs')
        return self._get(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_devicehapair(self, devicehapair_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devicehapairs/ftddevicehapairs/{devicehapair_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def update_devicehapair(self, data: Dict, devicehapair_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devicehapairs/ftddevicehapairs/{devicehapair_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def delete_devicehapair(self, devicehapair_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devicehapairs/ftddevicehapairs/{devicehapair_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_devicehapair_monitoredinterfaces(self, devicehapair_id: str):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devicehapairs/ftddevicehapairs/{devicehapair_id}/monitoredinterfaces'
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_devicehapair_monitoredinterface(self, devicehapair_id: str, monitoredinterface_id: str):
        url = self._url(
            defaults.API_CONFIG_NAME,
            f'/devicehapairs/ftddevicehapairs/{devicehapair_id}/monitoredinterfaces/{monitoredinterface_id}',
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def update_devicehapair_monitoredinterface(self, devicehapair_id: str, monitoredinterface_id: str, data: Dict):
        url = self._url(
            defaults.API_CONFIG_NAME,
            f'/devicehapairs/ftddevicehapairs/{devicehapair_id}/monitoredinterfaces/{monitoredinterface_id}',
        )
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_physicalinterfaces(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/physicalinterfaces')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_physicalinterface(self, device_id: str, interface_id: str):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/physicalinterfaces/{interface_id}'
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_device_physicalinterface(self, device_id: str, interface_id: str, data: Dict):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/physicalinterfaces/{interface_id}'
        )
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def create_device_redundantinterface(self, device_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/redundantinterfaces')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_redundantinterfaces(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/redundantinterfaces')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_redundantinterface(self, device_id: str, interface_id: str):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/redundantinterfaces/{interface_id}'
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_device_redundantinterface(self, device_id: str, interface_id: str, data: Dict):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/redundantinterfaces/{interface_id}'
        )
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def delete_device_redundantinterface(self, device_id: str, interface_id: str):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/redundantinterfaces/{interface_id}'
        )
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def create_device_inlineset(self, device_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/inlinesets')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_inlinesets(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/inlinesets')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_inlineset(self, device_id: str, inlineset_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/inlinesets/{inlineset_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_device_inlineset(self, device_id: str, inlineset_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/inlinesets/{inlineset_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def delete_device_inlineset(self, device_id: str, inlineset_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/inlinesets/{inlineset_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def create_device_etherchannelinterface(self, device_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/etherchannelinterfaces')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_etherchannelinterfaces(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/etherchannelinterfaces')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_etherchannelinterface(self, device_id: str, interface_id: str):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/etherchannelinterfaces/{interface_id}'
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_device_etherchannelinterface(self, device_id: str, interface_id: str, data: Dict):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/etherchannelinterfaces/{interface_id}'
        )
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def delete_device_etherchannelinterface(self, device_id: str, interface_id: str):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/etherchannelinterfaces/{interface_id}'
        )
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def create_device_subinterface(self, device_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/subinterfaces')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_subinterfaces(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/subinterfaces')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_device_subinterface(self, device_id: str, interface_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/subinterfaces/{interface_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_device_subinterface(self, device_id: str, interface_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/subinterfaces/{interface_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def delete_device_subinterface(self, device_id: str, interface_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/subinterfaces/{interface_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def create_device_vlaninterface(self, device_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/vlaninterfaces')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_device_vlaninterfaces(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/vlaninterfaces')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_device_vlaninterface(self, device_id: str, interface_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/vlaninterfaces/{interface_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def update_device_vlaninterface(self, device_id: str, interface_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/vlaninterfaces/{interface_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def delete_device_vlaninterface(self, device_id: str, interface_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/vlaninterfaces/{interface_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def create_device_ipv4staticroute(self, device_id: str, data: Dict, virtualrouter_id=''):
        url = self._virtualrouter_url(
            self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes')
        )
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_device_ipv4staticroutes(self, device_id: str, virtualrouter_id=''):
        url = self._virtualrouter_url(
            self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes')
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_device_ipv4staticroute(self, device_id: str, route_id: str, virtualrouter_id=''):
        url = self._virtualrouter_url(
            self._url(
                defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes/{route_id}'
            )
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def update_device_ipv4staticroute(self, device_id: str, route_id: str, data: Dict, virtualrouter_id=''):
        url = self._virtualrouter_url(
            self._url(
                defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes/{route_id}'
            )
        )
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def delete_device_ipv4staticroute(self, device_id: str, route_id: str, virtualrouter_id=''):
        url = self._virtualrouter_url(
            self._url(
                defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes/{route_id}'
            )
        )
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def create_device_ipv6staticroute(self, device_id: str, data: Dict):
        url = self._virtualrouter_url(
            self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes')
        )
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_device_ipv6staticroutes(self, device_id: str):
        url = self._virtualrouter_url(
            self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes')
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_device_ipv6staticroute(self, device_id: str, route_id: str):
        url = self._virtualrouter_url(
            self._url(
                defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes/{route_id}'
            )
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def update_device_ipv6staticroute(self, device_id: str, route_id: str, data: Dict):
        url = self._virtualrouter_url(
            self._url(
                defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes/{route_id}'
            )
        )
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def delete_device_ipv6staticroute(self, device_id: str, route_id: str):
        url = self._virtualrouter_url(
            self._url(
                defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes/{route_id}'
            )
        )
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_660)
    def create_device_virtualrouter(self, device_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/virtualrouters')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_660)
    def get_device_virtualrouters(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/virtualrouters')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_660)
    def get_device_virtualrouter(self, device_id: str, virtualrouter_id: str):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/virtualrouters/{virtualrouter_id}'
        )
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_660)
    def update_device_virtualrouter(self, device_id: str, virtualrouter_id: str, data: Dict):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/virtualrouters/{virtualrouter_id}'
        )
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_660)
    def delete_device_virtualrouter(self, device_id: str, virtualrouter_id: str):
        url = self._url(
            defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/routing/virtualrouters/{virtualrouter_id}'
        )
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def copy_device_configuration(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/devices/copyconfigrequests')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_device_interfaceevents(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/interfaceevents')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def accept_device_interfaces(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/interfaceevents')
        data = {'action': 'ACCEPT_CHANGES'}
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def sync_device_interfaces(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/interfaceevents')
        data = {'action': 'SYNC_WITH_DEVICE'}
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_660)
    def get_device_metrics(self, device_id: str, metric: str):
        params = {'filter': self._filter({'metric': metric})}
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/operational/metrics')
        return self._get(url, params)

    @utils.minimum_version_required(defaults.API_RELEASE_660)
    def device_command(self, device_id: str, command: str):
        # commands with wordsize > 2 must be split into filter and parameters params due to fmc rest api impl
        split_cmd = command.split(' ')
        filter_str = ' '.join(split_cmd[:2])
        params_str = ' '.join(split_cmd[2:])
        params = {'filter': self._filter({'command': filter_str}), 'parameters': params_str}
        url = self._url(defaults.API_CONFIG_NAME, f'/devices/devicerecords/{device_id}/operational/commands')
        return self._get(url, params)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def deploy(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/deployment/deploymentrequests')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_deployabledevices(self):
        url = self._url(defaults.API_CONFIG_NAME, '/deployment/deployabledevices')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_660)
    def get_pendingchanges(self, device_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/deployment/deployabledevices/{device_id}/pendingchanges')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_filepolicies(self):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/filepolicies')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_filepolicy(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/filepolicies/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_intrusionpolicies(self):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/intrusionpolicies')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_intrusionpolicy(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/intrusionpolicies/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def create_accesspolicy(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/accesspolicies')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_accesspolicies(self):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/accesspolicies')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_accesspolicy(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_accesspolicy(self, policy_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def delete_accesspolicy(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_accesspolicy_defaultactions(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/defaultactions')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_accesspolicy_defaultaction(self, policy_id: str, object_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/defaultactions/{object_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_accesspolicy_defaultaction(self, policy_id: str, object_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/defaultactions/{object_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_accesspolicy_loggingsettings(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/loggingsettings')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_accesspolicy_loggingsetting(self, policy_id: str, object_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/loggingsettings/{object_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def update_accesspolicy_loggingsetting(self, policy_id: str, object_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/loggingsettings/{object_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def create_accesspolicy_category(
        self, policy_id: str, data: Dict, section=None, above_category=None, insert_before=None, insert_after=None
    ):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/categories')
        params = {
            'aboveCategory': above_category,
            'section': section,
            'insertBefore': insert_before,
            'insertAfter': insert_after,
        }
        return self._post(url, data, params)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_accesspolicy_categories(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/categories')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_accesspolicy_category(self, policy_id: str, category_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/categories/{category_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def update_accesspolicy_category(self, policy_id: str, category_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/categories/{category_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def delete_accesspolicy_category(self, policy_id: str, category_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/categories/{category_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_accesspolicy_inheritancesettings(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/inheritancesettings')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_accesspolicy_inheritancesetting(self, policy_id: str, object_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/inheritancesettings/{object_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def update_accesspolicy_inheritancesetting(self, policy_id: str, object_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/inheritancesettings/{object_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_621)
    def create_accesspolicy_rule(
        self, policy_id: str, data: Dict, section='', category='', insert_before=None, insert_after=None,
    ):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/accessrules')
        params = {
            'category': category,
            'section': section,
            'insertBefore': insert_before,
            'insertAfter': insert_after,
        }
        return self._post(url, data, params)

    @utils.minimum_version_required(defaults.API_RELEASE_621)
    def create_accesspolicy_rules(
        self, policy_id: str, data: Dict, section=None, category=None, insert_before=None, insert_after=None,
    ):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/accessrules')
        params = {
            'bulk': True,
            'category': category,
            'section': section,
            'insertBefore': insert_before,
            'insertAfter': insert_after,
        }
        return self._post(url, data, params)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_accesspolicy_rule(self, policy_id: str, rule_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/accessrules/{rule_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_accesspolicy_rules(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/accessrules')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_accesspolicy_rule(self, policy_id: str, rule_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/accessrules/{rule_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def delete_accesspolicy_rule(self, policy_id: str, rule_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/accessrules/{rule_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def create_prefilterpolicy(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/prefilterpolicies')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_prefilterpolicies(self):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/prefilterpolicies')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_prefilterpolicy(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def update_prefilterpolicy(self, policy_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def delete_prefilterpolicy(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_prefilterpolicy_defaultactions(self, policy_id: str, object_id=''):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/defaultactions/{object_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def update_prefilterpolicy_defaultaction(self, policy_id: str, object_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/defaultactions/{object_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def create_prefilterpolicy_rule(
        self, policy_id: str, data: Dict, section=None, category=None, insert_before=None, insert_after=None,
    ):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/prefilterrules')
        params = {
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after,
        }
        return self._post(url, data, params)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def create_prefilterpolicy_rules(
        self, policy_id: str, data: Dict, section='', category='', insert_before=None, insert_after=None,
    ):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/prefilterrules')
        params = {
            'bulk': True,
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after,
        }
        return self._post(url, data, params)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_prefilterpolicy_rule(self, policy_id: str, rule_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/prefilterrules/{rule_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_prefilterpolicy_rules(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/prefilterrules')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def update_prefilterpolicy_rule(self, policy_id: str, rule_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/prefilterrules/{rule_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def delete_prefilterpolicy_rule(self, policy_id: str, rule_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/prefilterrules/{rule_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def create_natpolicy(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/ftdnatpolicies')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_natpolicies(self):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/ftdnatpolicies')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_natpolicy(self, policy_id):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def update_natpolicy(self, policy_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def delete_natpolicy(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def create_autonatrule(self, policy_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}/autonatrules')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_autonatrule(self, policy_id: str, rule_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}/autonatrules/{rule_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_autonatrules(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}/autonatrules')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def update_autonatrule(self, policy_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}/autonatrules')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def delete_autonatrule(self, policy_id: str, rule_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}/autonatrules/{rule_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def create_manualnatrule(self, policy_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}/manualnatrules')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_manualnatrule(self, policy_id: str, rule_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}/manualnatrules/{rule_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def get_manualnatrules(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/manualnatrules/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def update_manualnatrule(self, policy_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}/manualnatrules')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_623)
    def delete_manualnatrule(self, policy_id: str, rule_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftdnatpolicies/{policy_id}/manualnatrules/{rule_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def create_policyassignment(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/assignment/policyassignments')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_policyassignments(self):
        url = self._url(defaults.API_CONFIG_NAME, '/assignment/policyassignments')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_policyassignment(self, policy_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/assignment/policyassignments/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def update_policyassignment(self, policy_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/assignment/policyassignments/{policy_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_accesspolicy_hitcounts(self, policy_id: str, device_id: str, rule_ids=None, fetch_zero_hitcount=True):
        params = {
            'filter': self._filter({'deviceId': device_id, 'ids': rule_ids, 'fetchZeroHitCount': fetch_zero_hitcount})
        }
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/operational/hitcounts')
        return self._get(url, params)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def update_accesspolicy_hitcounts(self, policy_id: str, device_id: str, rule_ids=None):
        params = {'filter': self._filter({'deviceId': device_id, 'ids': rule_ids})}
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/operational/hitcounts')
        return self._put(url, params)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def delete_accesspolicy_hitcounts(self, policy_id: str, device_id: str, rule_ids=None):
        params = {'filter': self._filter({'deviceId': device_id, 'ids': rule_ids})}
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/accesspolicies/{policy_id}/operational/hitcounts')
        return self._put(url, params)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_prefilterpolicy_hitcounts(self, policy_id: str, device_id: str, rule_ids=None, fetch_zero_hitcount=True):
        params = {
            'filter': self._filter({'deviceId': device_id, 'ids': rule_ids, 'fetchZeroHitCount': fetch_zero_hitcount})
        }
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/operational/hitcounts')
        return self._get(url, params)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def update_prefilterpolicy_hitcounts(self, policy_id: str, device_id: str, rule_ids=None):
        params = {'filter': self._filter({'deviceId': device_id, 'ids': rule_ids})}
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/operational/hitcounts')
        return self._put(url, params)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def delete_prefilterpolicy_hitcounts(self, policy_id: str, device_id: str, rule_ids=None):
        params = {'filter': self._filter({'deviceId': device_id, 'ids': rule_ids})}
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/prefilterpolicies/{policy_id}/operational/hitcounts')
        return self._put(url, params)

    @utils.minimum_version_required(defaults.API_RELEASE_610)
    def get_taskstatus(self, task_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/job/taskstatuses/{task_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_upgradepackages(self):
        url = self._url(defaults.API_PLATFORM_NAME, '/updates/upgradepackages')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_upgradepackage(self, package_id: str):
        url = self._url(defaults.API_PLATFORM_NAME, f'/updates/upgradepackages/{package_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_upgradepackage_applicabledevices(self, package_id: str):
        url = self._url(defaults.API_PLATFORM_NAME, f'/updates/upgradepackages/{package_id}/applicabledevices')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def delete_upgradepackage(self, package_id: str):
        url = self._url(defaults.API_PLATFORM_NAME, f'/updates/upgradepackages/{package_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def install_upgradepackage(self, data: Dict):
        url = self._url(defaults.API_PLATFORM_NAME, '/updates/upgrades')
        return self._post(url)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_cloudeventsconfigs(self):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/cloudeventsconfigs')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_cloudeventsconfig(self, object_id: str):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/cloudeventsconfigs/{object_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def update_cloudeventsconfig(self, object_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/cloudeventsconfigs/{object_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def create_externallookup(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/externallookups')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_externallookups(self):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/externallookups')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def get_externallookup(self, object_id: str):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/externallookups/{object_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_640)
    def update_externallookup(self, object_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/externallookups/{object_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_cloudregions(self):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/cloudregions')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def get_cloudregion(self, object_id: str):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/cloudregions/{object_id}')
        return self._get(url)

    @utils.minimum_version_required(defaults.API_RELEASE_650)
    def update_cloudregion(self, object_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/integration/cloudregions/{object_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def create_s2svpn(self, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, '/policy/ftds2svpns')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_s2svpns(self, data: Dict, vpn_id=''):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def update_s2svpn(self, vpn_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def delete_s2svpn(self, vpn_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def create_s2svpn_endpoint(self, vpn_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/endpoints')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_s2svpn_endpoints(self, data: Dict, vpn_id: str, endpoint_id=''):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/endpoints/{endpoint_id}')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def update_s2svpn_endpoint(self, vpn_id: str, endpoint_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/endpoints/{endpoint_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def delete_s2svpn_endpoint(self, vpn_id: str, endpoint_id: str):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/endpoints/{endpoint_id}')
        return self._delete(url)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_s2svpn_ikesettings(self, data: Dict, vpn_id: str, ikesettings_id=''):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/ikesettings/{ikesettings_id}')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def update_s2svpn_ikesettings(self, vpn_id: str, ikesettings_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/ikesettings/{ikesettings_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_s2svpn_ipsecsettings(self, data: Dict, vpn_id: str, ipsecsettings_id=''):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/ipsecsettings/{ipsecsettings_id}')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def update_s2svpn_ipsecsettings(self, vpn_id: str, ipsecsettings_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/ipsecsettings/{ipsecsettings_id}')
        return self._put(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def get_s2svpn_advancedsettings(self, data: Dict, vpn_id: str, advancedsettings_id=''):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/advancedsettings/{advancedsettings_id}')
        return self._post(url, data)

    @utils.minimum_version_required(defaults.API_RELEASE_630)
    def update_s2svpn_advancedsettings(self, vpn_id: str, advancedsettings_id: str, data: Dict):
        url = self._url(defaults.API_CONFIG_NAME, f'/policy/ftds2svpns/{vpn_id}/advancedsettings/{advancedsettings_id}')
        return self._put(url, data)
