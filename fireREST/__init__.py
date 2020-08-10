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
        self.domain = self.get_domain_id_by_name(domain)
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
        return options[namespace]

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
            data=data,
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

    def _create(self, url: str, data: Dict, params=None):
        '''
        CREATE operation
        : param url: request that should be performed
        : param json: dictionary of data that will be sent to the api
        : param params: dict of parameters for http request
        : return: requests.Response object
        '''
        data = self._sanitize(data)
        return self._request('post', url, params=params, data=data)

    def _update(self, url: str, data: Dict, params=None):
        '''
        UPDATE operation
        : param url: request that should be performed
        : param json: dictionary of data that will be sent to the api
        : param params: dict of parameters for http request
        : return: requests.Response object
        '''
        data = self._sanitize(data)
        return self._request(url, data=data, params=params)

    def _sanitize(self, payload: Dict):
        '''
        Prepare json object for api operation
        This is neccesarry since fmc api cannot handle json objects with some
        fields set in GET (e.g. metadata dictionary)
        : param payload: api object in json format
        : return: sanitized api object in json format
        '''
        sanitized_payload = deepcopy(payload)
        sanitized_payload.pop('metadata', None)
        sanitized_payload.pop('links', None)
        sanitized_payload.pop('id', None)
        return sanitized_payload

    @utils.cache_result
    @utils.minimum_version_required('6.1.0')
    def get_object_id_by_name(self, object_type: str, object_name: str):
        '''
        helper function to retrieve object id by name
        : param object_type: object type that will be queried
        : param object_name: name of the object
        : return: object id if object is found, None otherwise
        '''
        request = f'/object/{object_type}'
        url = self._url('config', request)
        objects = self._get(url)
        for obj in objects:
            if obj['name'] == object_name:
                return obj['id']
        return None

    @utils.cache_result
    @utils.minimum_version_required('6.1.0')
    def get_device_id_by_name(self, device_name: str):
        '''
        helper function to retrieve device id by name
        : param device_name: name of the device
        : return: device id if device is found, None otherwise
        '''
        request = '/devices/devicerecords'
        url = self._url('config', request)
        devices = self._get(url)
        for device in devices:
            if device['name'] == device_name:
                return device['id']
        return None

    @utils.cache_result
    @utils.minimum_version_required('6.2.3')
    def get_device_hapair_id_by_name(self, device_hapair_name: str):
        '''
        helper function to retrieve device ha - pair id by name
        : param device_hapair_name: name of the ha - pair
        : return: id if ha - pair is found, None otherwise
        '''
        request = '/devicehapairs/ftddevicehapairs'
        url = self._url('config', request)
        ha_pairs = self._get(url)
        for ha_pair in ha_pairs:
            if ha_pair['name'] == device_hapair_name:
                return ha_pair['id']
        return None

    @utils.cache_result
    @utils.minimum_version_required('6.2.3')
    def get_device_id_from_hapair(self, device_hapair_id: str):
        '''
        helper function to retrieve device id from ha - pair
        : param device_hapar_id: id of ha - pair
        : return: id if device is found, None otherwise
        '''
        request = f'/devicehapairs/ftddevicehapairs/{device_hapair_id}'
        url = self._url('config', request)
        ha_pair = self._get(url)
        return ha_pair['primary']['id']

    @utils.cache_result
    @utils.minimum_version_required('6.2.3')
    def get_nat_policy_id_by_name(self, nat_policy_name: str):
        '''
        helper function to retrieve nat policy id by name
        : param nat_policy_name: name of nat policy
        : return: policy id if nat policy is found, None otherwise
        '''
        request = '/policy/ftdnatpolicies'
        url = self._url('config', request)
        nat_policies = self._get(url)
        for nat_policy in nat_policies:
            if nat_policy['name'] == nat_policy_name:
                return nat_policy['id']
        return None

    @utils.cache_result
    @utils.minimum_version_required('6.1.0')
    def get_accesspolicy_id_by_name(self, policy_name: str):
        '''
        helper function to retrieve access control policy id by name
        : param policy_name: name of the access control policy
        : return: accesspolicy id if access control policy is found, None otherwise
        '''
        request = '/policy/accesspolicies'
        url = self._url('config', request)
        accesspolicies = self._get(url)
        for accesspolicy in accesspolicies:
            if accesspolicy['name'] == policy_name:
                return accesspolicy['id']
        return None

    @utils.cache_result
    @utils.minimum_version_required('6.1.0')
    def get_accessrule_id_by_name(self, policy_name: str, rule_name: str):
        '''
        helper function to retrieve access control policy rule id by name
        : param policy_name: name of the access control policy that will be queried
        : param rule_name: name of the access control policy rule
        : return: accesspolicy rule id if access control policy rule is found, None otherwise
        '''
        policy_id = self.get_accesspolicy_id_by_name(policy_name)
        request = f'/policy/accesspolicies/{policy_id}/accessrules'
        url = self._url('config', request)
        accessrules = self._get(url)
        for accessrule in accessrules:
            if accessrule['name'] == rule_name:
                return accessrule['id']
        return None

    @utils.cache_result
    @utils.minimum_version_required('6.1.0')
    def get_syslog_alert_id_by_name(self, syslog_alert_name: str):
        '''
        helper function to retrieve syslog alert object id by name
        : param syslog_alert_name: name of syslog alert object
        : return: syslogalert id if syslog alert is found, None otherwise
        '''
        syslogalerts = self.get_syslogalerts()
        for syslog_alert in syslogalerts:
            if syslog_alert['name'] == syslog_alert_name:
                return syslog_alert['id']
        return None

    @utils.cache_result
    @utils.minimum_version_required('6.1.0')
    def get_snmp_alert_id_by_name(self, snmp_alert_name: str):
        '''
        helper function to retrieve snmp alert object id by name
        : param snmp_alert_name: name of snmp alert object
        : return: snmpalert id if snmp alert is found, None otherwise
        '''
        snmp_alerts = self.get_snmpalerts()
        for snmp_alert in snmp_alerts:
            if snmp_alert['name'] == snmp_alert_name:
                return snmp_alert['id']
        return None

    def get_domain_id_by_name(self, domain_name: str):
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

    @utils.minimum_version_required('6.1.0')
    def get_system_version(self):
        url = self._url('platform', '/info/serverversion')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_audit_records(self):
        url = self._url('config', '/audit/auditrecords')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_syslogalerts(self):
        url = self._url('config', '/policy/syslogalerts')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_snmpalerts(self):
        url = self._url('config', '/policy/snmpalerts')
        return self._get(url)

    @utils.validate_object_type
    @utils.minimum_version_required('6.1.0')
    def create_object(self, object_type: str, data: Dict):
        url = self._url('config', f'/object/{object_type}')
        return self._create(url, data)

    @utils.validate_object_type
    @utils.minimum_version_required('6.1.0')
    def get_objects(self, object_type: str):
        url = self._url('config', f'/object/{object_type}')
        return self._get(url)

    @utils.validate_object_type
    @utils.minimum_version_required('6.4.0')
    def get_objects_override(self, object_type: str, objects: List):
        overrides = []
        for obj in objects:
            if obj['overridable']:
                responses = self.get_object_override(object_type, obj['id'])
                overrides.extend(responses)
        return overrides

    @utils.validate_object_type
    @utils.minimum_version_required('6.1.0')
    def get_object(self, object_type: str, object_id: str):
        url = self._url('config', f'/object/{object_type}/{object_id}')
        return self._get(url)

    @utils.validate_object_type
    @utils.minimum_version_required('6.4.0')
    def get_object_override(self, object_type: str, object_id: str):
        url = self._url('config', f'/object/{object_type}/{object_id}/overrides')
        return self._get(url)

    @utils.validate_object_type
    @utils.minimum_version_required('6.1.0')
    def update_object(self, object_type: str, object_id: str, data: Dict):
        url = self._url('config', f'/object/{object_type}/{object_id}')
        return self._update(url, data)

    @utils.validate_object_type
    @utils.minimum_version_required('6.1.0')
    def delete_object(self, object_type: str, object_id: str):
        url = self._url('config', f'/object/{object_type}/{object_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.1.0')
    def create_device(self, data: Dict):
        url = self._url('config', '/devices/devicerecords')
        return self._create(url, data)

    @utils.minimum_version_required('6.1.0')
    def get_devices(self):
        url = self._url('config', '/devices/devicerecords')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_device(self, device_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def update_device(self, device_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}')
        return self._update(url, data)

    @utils.minimum_version_required('6.1.0')
    def delete_device(self, device_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.2.3')
    def get_device_hapairs(self):
        url = self._url('config', '/devicehapairs/ftddevicehapairs')
        return self._get(url)

    @utils.minimum_version_required('6.2.3')
    def create_device_hapair(self, data: Dict):
        url = self._url('config', '/devicehapairs/ftddevicehapairs')
        return self._get(url, data)

    @utils.minimum_version_required('6.2.3')
    def get_device_hapair(self, device_hapair_id: str):
        url = self._url('config', f'/devicehapairs/ftddevicehapairs/{device_hapair_id}')
        return self._get(url)

    @utils.minimum_version_required('6.2.3')
    def update_device_hapair(self, data: Dict, device_hapair_id: str):
        url = self._url('config', f'/devicehapairs/ftddevicehapairs/{device_hapair_id}')
        return self._update(url, data)

    @utils.minimum_version_required('6.2.3')
    def delete_device_hapair(self, device_hapair_id: str):
        url = self._url('config', f'/devicehapairs/ftddevicehapairs/{device_hapair_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.3.0')
    def get_device_hapair_monitoredinterfaces(self, device_hapair_id: str):
        url = self._url('config', f'/devicehapairs/ftddevicehapairs/{device_hapair_id}/monitoredinterfaces',)
        return self._get(url)

    @utils.minimum_version_required('6.3.0')
    def get_device_hapair_monitoredinterface(self, device_hapair_id: str, monitoredinterface_id: str):
        url = self._url(
            'config', f'/devicehapairs/ftddevicehapairs/{device_hapair_id}/monitoredinterfaces/{monitoredinterface_id}',
        )
        return self._get(url)

    @utils.minimum_version_required('6.3.0')
    def update_device_hapair_monitoredinterface(self, device_hapair_id: str, monitoredinterface_id: str, data: Dict):
        url = self._url(
            'config', f'/devicehapairs/ftddevicehapairs/{device_hapair_id}/monitoredinterfaces/{monitoredinterface_id}',
        )
        return self._update(url, data)

    @utils.minimum_version_required('6.1.0')
    def get_ftd_physical_interfaces(self, device_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/physicalinterfaces')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_ftd_physical_interface(self, device_id: str, interface_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/physicalinterfaces/{interface_id}',)
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def update_ftd_physical_interface(self, device_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/physicalinterfaces')
        return self._update(url, data)

    @utils.minimum_version_required('6.1.0')
    def create_ftd_redundant_interface(self, device_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/redundantinterfaces')
        return self._create(url, data)

    @utils.minimum_version_required('6.1.0')
    def get_ftd_redundant_interfaces(self, device_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/redundantinterfaces')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_ftd_redundant_interface(self, device_id: str, interface_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/redundantinterfaces/{interface_id}',)
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def update_ftd_redundant_interface(self, device_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/redundantinterfaces')
        return self._update(url, data)

    @utils.minimum_version_required('6.1.0')
    def delete_ftd_redundant_interface(self, device_id: str, interface_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/redundantinterfaces/{interface_id}',)
        return self._delete(url)

    @utils.minimum_version_required('6.1.0')
    def create_ftd_portchannel_interface(self, device_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/etherchannelinterfaces')
        return self._create(url, data)

    @utils.minimum_version_required('6.1.0')
    def get_ftd_portchannel_interfaces(self, device_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/etherchannelinterfaces')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_ftd_portchannel_interface(self, device_id: str, interface_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/etherchannelinterfaces/{interface_id}',)
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def update_ftd_portchannel_interface(self, device_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/etherchannelinterfaces')
        return self._update(url, data)

    @utils.minimum_version_required('6.1.0')
    def delete_ftd_portchannel_interface(self, device_id: str, interface_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/etherchannelinterfaces/{interface_id}',)
        return self._delete(url)

    @utils.minimum_version_required('6.1.0')
    def create_ftd_sub_interface(self, device_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/subinterfaces')
        return self._create(url, data)

    @utils.minimum_version_required('6.1.0')
    def get_ftd_sub_interfaces(self, device_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/subinterfaces')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_ftd_sub_interface(self, device_id: str, interface_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/subinterfaces/{interface_id}')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def update_ftd_sub_interface(self, device_id: str, interface_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/subinterfaces/{interface_id}')
        return self._update(url, data)

    @utils.minimum_version_required('6.1.0')
    def delete_ftd_sub_interface(self, device_id: str, interface_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/subinterfaces/{interface_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.3.0')
    def create_ftd_ipv4staticroute(self, device_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes')
        return self._create(url, data)

    @utils.minimum_version_required('6.3.0')
    def get_ftd_ipv4staticroutes(self, device_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes')
        return self._get(url)

    @utils.minimum_version_required('6.3.0')
    def get_ftd_ipv4staticroute(self, device_id: str, route_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes/{route_id}',)
        return self._get(url)

    @utils.minimum_version_required('6.3.0')
    def update_ftd_ipv4staticroute(self, device_id: str, route_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes/{route_id}',)
        return self._update(url, data)

    @utils.minimum_version_required('6.3.0')
    def delete_ftd_ipv4staticroute(self, device_id: str, route_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes/{route_id}',)
        return self._delete(url)

    @utils.minimum_version_required('6.3.0')
    def create_ftd_ipv6staticroute(self, device_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes')
        return self._create(url, data)

    @utils.minimum_version_required('6.3.0')
    def get_ftd_ipv6staticroutes(self, device_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes')
        return self._get(url)

    @utils.minimum_version_required('6.3.0')
    def get_ftd_ipv6staticroute(self, device_id: str, route_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes/{route_id}',)
        return self._get(url)

    @utils.minimum_version_required('6.3.0')
    def update_ftd_ipv6staticroute(self, device_id: str, route_id: str, data: Dict):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes/{route_id}',)
        return self._update(url, data)

    @utils.minimum_version_required('6.3.0')
    def delete_ftd_ipv6staticroute(self, device_id: str, route_id: str):
        url = self._url('config', f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes/{route_id}',)
        return self._delete(url)

    @utils.minimum_version_required('6.1.0')
    def deploy(self, data: Dict):
        url = self._url('config', '/deployment/deploymentrequests')
        return self._create(url, data)

    @utils.minimum_version_required('6.1.0')
    def get_deployable_devices(self):
        url = self._url('config', '/deployment/deployabledevices')
        return self._get(url)

    @utils.minimum_version_required('6.6.0')
    def get_pendingchanges(self, device_id: str):
        url = self._url('config', f'/deployment/deployabledevices/{device_id}/pendingchanges')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def create_accesspolicy(self, data: Dict):
        url = self._url('config', f'/policy/accesspolicies')
        return self._create(url, data)

    @utils.minimum_version_required('6.1.0')
    def get_accesspolicies(self):
        url = self._url('config', f'/policy/accesspolicies')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_accesspolicy(self, policy_id: str):
        url = self._url('config', f'/policy/accesspolicies/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def update_accesspolicy(self, policy_id: str, data: Dict):
        url = self._url('config', f'/policy/accesspolicies/{policy_id}')
        return self._update(url, data)

    @utils.minimum_version_required('6.1.0')
    def delete_accesspolicy(self, policy_id: str):
        url = self._url('config', f'/policy/accesspolicies/{policy_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.2.1')
    def create_accessrule(
        self, policy_id: str, data: Dict, section='', category='', insert_before=None, insert_after=None,
    ):
        url = self._url('config', f'/policy/accesspolicies/{policy_id}/accessrules')
        params = {
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after,
        }
        return self._create(url, data, params)

    @utils.minimum_version_required('6.2.1')
    def create_accessrules(
        self, policy_id: str, data: Dict, section='', category='', insert_before=None, insert_after=None,
    ):
        url = self._url('config', f'/policy/accesspolicies/{policy_id}/accessrules')
        params = {
            'bulk': True,
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after,
        }
        return self._create(url, data, params)

    @utils.minimum_version_required('6.1.0')
    def get_accessrule(self, policy_id: str, rule_id: str):
        url = self._url('config', f'/policy/accesspolicies/{policy_id}/accessrules/{rule_id}')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_accessrules(self, policy_id: str):
        url = self._url('config', f'/policy/accesspolicies/{policy_id}/accessrules')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def update_accessrule(self, policy_id: str, rule_id: str, data: Dict):
        url = self._url('config', f'/policy/accesspolicies/{policy_id}/accessrules/{rule_id}')
        return self._update(url, data)

    @utils.minimum_version_required('6.1.0')
    def delete_accessrule(self, policy_id: str, rule_id: str):
        url = self._url('config', f'/policy/accesspolicies/{policy_id}/accessrules/{rule_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.5.0')
    def create_prefilterpolicy(self, data: Dict):
        url = self._url('config', f'/policy/prefilterpolicies')
        return self._create(url, data)

    @utils.minimum_version_required('6.5.0')
    def get_prefilterpolicies(self):
        url = self._url('config', f'/policy/prefilterpolicies')
        return self._get(url)

    @utils.minimum_version_required('6.5.0')
    def get_prefilterpolicy(self, policy_id: str):
        url = self._url('config', f'/policy/prefilterpolicies/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required('6.5.0')
    def update_prefilterpolicy(self, policy_id: str, data: Dict):
        url = self._url('config', f'/policy/prefilterpolicies/{policy_id}')
        return self._update(url, data)

    @utils.minimum_version_required('6.5.0')
    def delete_prefilterpolicy(self, policy_id: str):
        url = self._url('config', f'/policy/prefilterpolicies/{policy_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.5.0')
    def create_prefilterrule(
        self, policy_id: str, data: Dict, section='', category='', insert_before=None, insert_after=None,
    ):
        url = self._url('config', f'/policy/prefilterpolicies/{policy_id}/prefilterrules')
        params = {
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after,
        }
        return self._create(url, data, params)

    @utils.minimum_version_required('6.5.0')
    def create_prefilterrules(
        self, policy_id: str, data: Dict, section='', category='', insert_before=None, insert_after=None,
    ):
        url = self._url('config', f'/policy/prefilterpolicies/{policy_id}/prefilterrules')
        params = {
            'bulk': True,
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after,
        }
        return self._create(url, data, params)

    @utils.minimum_version_required('6.5.0')
    def get_prefilterrule(self, policy_id: str, rule_id: str):
        url = self._url('config', f'/policy/prefilterpolicies/{policy_id}/prefilterrules/{rule_id}')
        return self._get(url)

    @utils.minimum_version_required('6.5.0')
    def get_prefilterrules(self, policy_id: str):
        url = self._url('config', f'/policy/prefilterpolicies/{policy_id}/prefilterrules')
        return self._get(url)

    @utils.minimum_version_required('6.5.0')
    def update_prefilterrule(self, policy_id: str, rule_id: str, data: Dict):
        url = self._url('config', f'/policy/prefilterpolicies/{policy_id}/prefilterrules/{rule_id}')
        return self._update(url, data)

    @utils.minimum_version_required('6.5.0')
    def delete_prefilterrule(self, policy_id: str, rule_id: str):
        url = self._url('config', f'/policy/prefilterpolicies/{policy_id}/prefilterrules/{rule_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.2.3')
    def create_autonat_rule(self, policy_id: str, data: Dict):
        url = self._url('config', f'/policy/ftdnatpolicies/{policy_id}/autonatrules')
        return self._create(url, data)

    @utils.minimum_version_required('6.2.3')
    def get_autonat_rule(self, policy_id: str, rule_id: str):
        url = self._url('config', f'/policy/ftdnatpolicies/{policy_id}/autonatrules/{rule_id}')
        return self._get(url)

    @utils.minimum_version_required('6.2.3')
    def get_autonat_rules(self, policy_id: str):
        url = self._url('config', f'/policy/ftdnatpolicies/{policy_id}/autonatrules')
        return self._get(url)

    @utils.minimum_version_required('6.2.3')
    def update_autonat_rule(self, policy_id: str, data: Dict):
        url = self._url('config', f'/policy/ftdnatpolicies/{policy_id}/autonatrules')
        return self._update(url, data)

    @utils.minimum_version_required('6.2.3')
    def delete_autonat_rule(self, policy_id: str, rule_id: str):
        url = self._url('config', f'/policy/ftdnatpolicies/{policy_id}/autonatrules/{rule_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.2.3')
    def create_manualnat_rule(self, policy_id: str, data: Dict):
        url = self._url('config', f'/policy/ftdnatpolicies/{policy_id}/manualnatrules')
        return self._create(url, data)

    @utils.minimum_version_required('6.2.3')
    def get_manualnat_rule(self, policy_id: str, rule_id: str):
        url = self._url('config', f'/policy/ftdnatpolicies/{policy_id}/manualnatrules/{rule_id}')
        return self._get(url)

    @utils.minimum_version_required('6.2.3')
    def get_manualnat_rules(self, policy_id: str):
        url = self._url('config', f'/policy/ftdnatpolicies/manualnatrules/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required('6.2.3')
    def update_manualnat_rule(self, policy_id: str, data: Dict):
        url = self._url('config', f'/policy/ftdnatpolicies/{policy_id}/manualnatrules')
        return self._update(url, data)

    @utils.minimum_version_required('6.2.3')
    def delete_manualnat_rule(self, policy_id: str, rule_id: str):
        url = self._url('config', f'/policy/ftdnatpolicies/{policy_id}/manualnatrules/{rule_id}')
        return self._delete(url)

    @utils.minimum_version_required('6.1.0')
    def create_policy_assignment(self, data: Dict):
        url = self._url('config', '/assignment/policyassignments')
        return self._create(url, data)

    @utils.minimum_version_required('6.1.0')
    def get_policy_assignments(self):
        url = self._url('config', '/assignment/policyassignments')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def get_policy_assignment(self, policy_id: str):
        url = self._url('config', f'/assignment/policyassignments/{policy_id}')
        return self._get(url)

    @utils.minimum_version_required('6.1.0')
    def update_policy_assignment(self, policy_id: str, data: Dict):
        url = self._url('config', f'/assignment/policyassignments/{policy_id}')
        return self._update(url, data)
