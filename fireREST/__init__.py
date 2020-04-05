import json
import logging
import requests
import urllib3

from .version import __version__

from http.client import responses as http_responses
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError
from time import sleep
from typing import Dict, List
from uuid import uuid4, UUID

#: protocol used to connect to api
API_PROTOCOL = 'https'

#: user agent sent to fmc
API_USER_AGENT = f'FireREST/{__version__}'

#: url used to generate token for api authorization
API_AUTH_URL = '/api/fmc_platform/v1/auth/generatetoken'

#: url used to refresh existing authorization token
API_REFRESH_URL = '/api/fmc_platform/v1/auth/refreshtoken'

#: url used to access platform related api calls
API_PLATFORM_URL = '/api/fmc_platform/v1'

#: url used to access configuration related api calls
API_CONFIG_URL = '/api/fmc_config/v1'

#: content type. as of 6.5.0 FMC only supports json
API_CONTENT_TYPE = 'application/json'

#: paging limit for get requests that contain multiple items
API_PAGING_LIMIT = 1000

#: expansion mode for get requests
API_EXPANSION_MODE = True

#: http request timeout
API_REQUEST_TIMEOUT = 120

#: name of fmc default domain for api requests
API_DEFAULT_DOMAIN = 'Global'

#: retry timer in seconds for repeating failed api calls
API_RETRY_TIMER = 10


class FireRESTApiException(Exception):
    '''
    generic api error exception
    '''

    def __init__(self, message):
        super().__init__(message)


class FireRESTAuthException(Exception):
    '''
    generic api authentication failure exception
    '''

    def __init__(self, message):
        super().__init__(message)


class FireRESTAuthRefreshException(Exception):
    '''
    exception used when api token refresh fails
    '''

    def __init__(self, message):
        super().__init__(message)


class FireRESTRateLimitException(Exception):
    '''
    exception used when fmc rate limiter kicks in
    '''

    def __init__(self, message):
        super().__init__(message)


class RequestDebugDecorator(object):
    '''
    decorator that adds additional debug logging for api requests
    '''

    def __init__(self, action):
        self.action = action

    def __call__(self, f):
        def wrapped_f(*args):
            action = self.action
            logger = args[0].logger
            request = args[1]
            request_id = str(uuid4())[:8]
            try:
                data = args[3]
            except IndexError:
                data = None
            logger.debug(f'[{request_id}] [{action}] {request}')
            if data:
                logger.debug(f'[{request_id}] [Data] {data}')
            result = f(*args)
            status_code = result.status_code
            status_code_name = http_responses[status_code]
            logger.debug(f'[{request_id}] [Response] {status_code_name} ({status_code})')
            if status_code >= 299:
                logger.debug(f'[{request_id}] [Message] {result.content}')
            return result

        return wrapped_f


class Client(object):
    def __init__(self, hostname: str, username: str, password: str, session=None, protocol=API_PROTOCOL,
                 verify_cert=False, logger=None, domain=API_DEFAULT_DOMAIN, timeout=API_REQUEST_TIMEOUT):
        '''
        Initialize api client object (make sure to use a dedicated api user!)
        :param hostname: ip address or dns name of fmc
        :param username: fmc username
        :param password: fmc password
        :param session: authentication session (can be provided in case api client should not generate one at init).
                      Make sure to pass the headers of a successful authentication to the session variable,
                      otherwise this will fail
        :param protocol: protocol used to access fmc api
        :param verify_cert: check fmc certificate for vailidity
        :param logger: optional logger instance, in case debug logging is needed
        :param domain: name of the fmc domain
        :param timeout: timeout value for http requests
        '''
        self.headers = {
            'Content-Type': API_CONTENT_TYPE,
            'Accept': API_CONTENT_TYPE,
            'User-Agent': API_USER_AGENT,
        }
        self.refresh_counter = 0
        self.logger = self._get_logger(logger)
        self.hostname = hostname
        self.protocol = protocol
        self.verify_cert = verify_cert
        self.timeout = timeout
        self.cred = HTTPBasicAuth(username, password)
        if not verify_cert:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        if not session:
            self._login()
        else:
            self.domains = session['domains']
            self.headers['X-auth-access-token'] = session['X-auth-access-token']
            self.headers['X-auth-refresh-token'] = session['X-auth-refresh-token']
        self.domain_name = domain
        self.domain = self.get_domain_id_by_name(domain)

    @staticmethod
    def _get_logger(logger: object):
        '''
        Generate dummy logger in case api client has been initialized without a logger
        :param logger: logger instance
        :return: dummy logger instance if logger is None, otherwise return logger variable again
        '''
        if not logger:
            dummy_logger = logging.getLogger(f'{API_USER_AGENT}.Client')
            dummy_logger.addHandler(logging.NullHandler())
            return dummy_logger
        return logger

    def _squash_responses(self, responses: List):
        if len(responses) == 1:
            payload = responses[0].json()

            # get request did not yield any results
            if not payload['links']:
                return list()

            # get request contains multiple results without paging
            if 'items' in payload:
                return payload['items']

            # get request returned single item
            return responses[0].json()
        items = list()
        for response in responses:
            if 'items' in response:
                items.extend(response.json()['items'])
            else:
                self.logger.debug('Response {response.url} did not contain any items. Skipping...')
        return items

    def _is_getbyid_operation(self, request: str):
        '''
        Verify if a get request contains multiple items
        :param request: request url
        :return: True if operation returns a single item, False if it contains multiple items
        '''
        try:
            val = UUID(request.split('/')[-1])  # noqa: F841
            return True
        except ValueError:
            if 'overrides' in request:
                return True
            return False

    def _url(self, namespace='base', path=str()):
        '''
        Generate URLs on the fly for requests to firepower api
        :param namespace: name of the url namespace that should be used. options: base, config, auth. default = base
        :param path: the url path for which a full url should be created
        :return: url in string format
        '''
        options = {
            'base': f'{self.protocol}://{self.hostname}{path}',
            'config': f'{self.protocol}://{self.hostname}{API_CONFIG_URL}/domain/{self.domain}{path}',
            'platform': f'{self.protocol}://{self.hostname}{API_PLATFORM_URL}{path}',
            'refresh': f'{self.protocol}://{self.hostname}{API_REFRESH_URL}',
        }
        if namespace not in options.keys():
            raise ValueError(f'Invalid namespace "{namespace}" provided. Valid namespaces: {options.keys()}')
        return options[namespace]

    def _login(self):
        '''
        Login to fmc api and save X-auth-access-token, X-auth-refresh-token and DOMAINS to variables
        '''
        request = f'{self.protocol}://{self.hostname}{API_AUTH_URL}'
        try:
            response = requests.post(request, headers=self.headers, auth=self.cred, verify=self.verify_cert)

            if response.status_code in (401, 403):
                self.logger.error(f'API Authentication to {self.hostname} failed.')
                raise FireRESTAuthException(f'API Authentication to {self.hostname} failed.')

            if response.status_code == 429:
                msg = f'API Authentication to {self.hostname} failed due to FMC rate limiting. Retrying in {API_RETRY_TIMER} seconds.'
                raise FireRESTRateLimitException(msg)
            access_token = response.headers.get('X-auth-access-token', default=None)
            refresh_token = response.headers.get('X-auth-refresh-token', default=None)
            if not access_token or not refresh_token:
                self.logger.error(f'Could not retrieve tokens from {request}.')
                raise FireRESTApiException(f'Could not retrieve tokens from {request}.')

            self.headers['X-auth-access-token'] = access_token
            self.headers['X-auth-refresh-token'] = refresh_token
            self.domains = json.loads(response.headers.get('DOMAINS', default=None))
            self.refresh_counter = 0
            self.logger.debug(f'Successfully authenticated to {self.hostname}')
        except ConnectionError as exc:
            self.logger.error(exc, exc_info=True)
            raise
        except FireRESTRateLimitException:
            self.logger.debug(
                f'Could not login to {self.hostname}. Rate limit exceeded. Retrying in {API_RETRY_TIMER} seconds.')
            sleep(API_RETRY_TIMER)
            self._login()

    def _refresh(self):
        '''
        Refresh X-auth-access-token using X-auth-refresh-token. This operation is performed for up to three
        times, afterwards a re-authentication using _login will be performed
        '''
        if self.refresh_counter > 2:
            self.logger.info(f'Authentication token expired. Re-authenticating to {self.hostname}')
            self._login()
            return

        request = self._url('refresh')
        try:
            self.refresh_counter += 1
            response = requests.post(request, headers=self.headers, verify=self.verify_cert)

            if response.status_code == 429:
                msg = f'API token refresh to {self.hostname} failed due to FMC rate limiting. Retrying in {API_RETRY_TIMER} seconds.'
                raise FireRESTRateLimitException(msg)

            access_token = response.headers.get('X-auth-access-token', default=None)
            refresh_token = response.headers.get('X-auth-refresh-token', default=None)
            if not access_token or not refresh_token:
                msg = f'API token refresh to {self.hostname} failed. Response Code: {response.status_code}'
                raise FireRESTAuthRefreshException(msg)

            self.headers['X-auth-access-token'] = access_token
            self.headers['X-auth-refresh-token'] = refresh_token
        except ConnectionError as exc:
            self.logger.error(exc, exc_info=True)
            raise
        except FireRESTRateLimitException:
            self.logger.debug(
                f'API token refresh to {self.hostname} failed. Rate limit exceeded. Retrying in {API_RETRY_TIMER} seconds.')
            sleep(API_RETRY_TIMER)
            self._login()
        except FireRESTApiException as exc:
            self.logger.error(str(exc))
            raise

        self.logger.debug(f'Successfully refreshed authorization token for {self.hostname}')

    @RequestDebugDecorator('DELETE')
    def _delete(self, request: str, params=None):
        '''
        DELETE Operation for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param params: dict of parameters for http request
        :return: requests.Response object
        '''
        if params is None:
            params = dict()
        try:
            response = requests.delete(request, headers=self.headers, params=params, verify=self.verify_cert,
                                       timeout=self.timeout)
            if response.status_code == 401:
                if 'Access token invalid' in str(response.json()):
                    self._refresh()
                    return self._delete(request, params)
            if response.status_code == 429:
                msg = f'DELETE operation {request} failed due to FMC rate limiting. Retrying in {API_RETRY_TIMER} seconds.'
                raise FireRESTRateLimitException(msg)
        except FireRESTRateLimitException:
            sleep(API_RETRY_TIMER)
            return self._delete(request, params)
        return response

    @RequestDebugDecorator('GET')
    def _get_request(self, request: str, params=None):
        '''
        GET Operation for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param params: dict of parameters for http request
        :return: requests.Response object
        '''
        if params is None:
            params = dict()
        if not self._is_getbyid_operation(request) and 'limit' not in params:
            params['limit'] = API_PAGING_LIMIT
        try:
            response = requests.get(request, headers=self.headers, params=params, verify=self.verify_cert,
                                    timeout=self.timeout)
            if response.status_code == 401:
                if 'Access token invalid' in str(response.json()):
                    self._refresh()
                    return self._get_request(request, params)
            if response.status_code == 429:
                msg = f'GET operation {request} failed due to FMC rate limiting. Retrying in {API_RETRY_TIMER} seconds.'
                raise FireRESTRateLimitException(msg)
        except FireRESTRateLimitException:
            sleep(API_RETRY_TIMER)
            return self._get_request(request, params)
        return response

    def _get(self, request: str, params=None):
        '''
        GET Operation that supports paging for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param params: dict of parameters for http request
        :return: list of requests.Response objects
        '''
        if params is None:
            params = dict()
        responses = list()
        response = self._get_request(request, params)
        responses.append(response)
        payload = response.json()
        if 'paging' in payload.keys():
            pages = int(payload['paging']['pages'])
            params['limit'] = int(payload['paging']['limit'])
            for i in range(1, pages, 1):
                params['offset'] = i * params['limit']
                response_page = self._get_request(request, params)
                responses.append(response_page)
        print(self._squash_responses(responses))
        return self._squash_responses(responses)

    @RequestDebugDecorator('POST')
    def _post(self, request: str, data: Dict, params=None):
        '''
        POST Operation for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param data: dictionary of data that will be sent to the api
        :param params: dict of parameters for http request
        :return: requests.Response object
        '''
        if params is None:
            params = dict()
        try:
            response = requests.post(request, data=json.dumps(data), headers=self.headers, params=params,
                                     verify=self.verify_cert, timeout=self.timeout)
            if response.status_code == 401:
                if 'Access token invalid' in str(response.json()):
                    self._refresh()
                    return self._post(request, data, params)
            if response.status_code == 429:
                msg = f'POST operation {request} failed due to FMC rate limiting. Retrying in {API_RETRY_TIMER} seconds.'
                raise FireRESTRateLimitException(msg)
        except FireRESTRateLimitException:
            sleep(API_RETRY_TIMER)
            return self._post(request, data, params)
        return response

    @RequestDebugDecorator('PUT')
    def _put(self, request: str, data: Dict, params=None):
        '''
        PUT Operation for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param data: dictionary of data that will be sent to the api
        :param params: dict of parameters for http request
        :return: requests.Response object
        '''
        if params is None:
            params = dict()
        try:
            response = requests.put(request, data=json.dumps(data), headers=self.headers, params=params,
                                    verify=self.verify_cert, timeout=self.timeout)
            if response.status_code == 401:
                if 'Access token invalid' in response.text:
                    self._refresh()
                    return self._put(request, data, params)
            if response.status_code == 429:
                msg = f'PUT operation {request} failed due to FMC rate limiting. Retrying in {API_RETRY_TIMER} seconds.'
                raise FireRESTRateLimitException(msg)
        except FireRESTRateLimitException:
            sleep(API_RETRY_TIMER)
            return self._put(request, data, params)
        return response

    def prepare_json(self, operation: str, obj_type: str, data: Dict):
        '''
        Prepare json object for api operation
        :param operation: PUT, POST
        :param obj_type: see supported types in schema.py
        :param data: json representing api object
        :return: sanatized api object
        '''
        return

    def get_object_id_by_name(self, obj_type: str, obj_name: str):
        '''
        helper function to retrieve object id by name
        :param obj_type: object types that will be queried
        :param obj_name:  name of the object
        :return: object id if object is found, None otherwise
        '''
        request = f'/object/{obj_type}'
        url = self._url('config', request)
        objects = self._get(url)
        for item in objects:
            if obj['name'] == obj_name:
                return obj['id']
        return None

    def get_device_id_by_name(self, device_name: str):
        '''
        helper function to retrieve device id by name
        :param device_name:  name of the device
        :return: device id if device is found, None otherwise
        '''
        request = '/devices/devicerecords'
        url = self._url('config', request)
        devices = self._get(url)
        for device in devices:
            if device['name'] == device_name:
                return device['id']
        return None

    def get_device_hapair_id_by_name(self, device_hapair_name: str):
        '''
        helper function to retrieve device ha-pair id by name
        :param device_hapair_name: name of the ha-pair
        :return: id if ha-pair is found, None otherwise
        '''
        request = '/devicehapairs/ftddevicehapairs'
        url = self._url('config', request)
        ha_pairs = self._get(url)
        for ha_pair in ha_pairs:
            if ha_pair['name'] == device_hapair_name:
                return ha_pair['id']
        return None

    def get_device_id_from_hapair(self, device_hapair_id: str):
        '''
        helper function to retrieve device id from ha-pair
        :param device_hapar_id: id of ha-pair
        :return: id if device is found, None otherwise
        '''
        request = f'/devicehapairs/ftddevicehapairs/{device_hapair_id}'
        url = self._url('config', request)
        ha_pair = self._get(url)
        return ha_pair['primary']['id']

    def get_nat_policy_id_by_name(self, nat_policy_name: str):
        '''
        helper function to retrieve nat policy id by name
        :param nat_policy_name: name of nat policy
        :return: policy id if nat policy is found, None otherwise
        '''
        request = '/policy/ftdnatpolicies'
        url = self._url('config', request)
        nat_policies = self._get(url)
        for nat_policy in nat_policies:
            if nat_policy['name'] == nat_policy_name:
                return nat_policy['id']
        return None

    def get_acp_id_by_name(self, policy_name: str):
        '''
        helper function to retrieve access control policy id by name
        :param policy_name:  name of the access control policy
        :return: acp id if access control policy is found, None otherwise
        '''
        request = '/policy/accesspolicies'
        url = self._url('config', request)
        accesspolicies = self._get(url)
        for accesspolicy in accesspolicies:
            if accesspolicy['name'] == policy_name:
                return accesspolicy['id']
        return None

    def get_acp_rule_id_by_name(self, policy_name: str, rule_name: str):
        '''
        helper function to retrieve access control policy rule id by name
        :param policy_name: name of the access control policy that will be queried
        :param rule_name:  name of the access control policy rule
        :return: acp rule id if access control policy rule is found, None otherwise
        '''
        policy_id = self.get_acp_id_by_name(policy_name)
        request = f'/policy/accesspolicies/{policy_id}/accessrules'
        url = self._url('config', request)
        acp_rules = self._get(url)
        for acp_rule in acp_rules:
            if acp_rule['name'] == rule_name:
                return acp_rule['id']
        return None

    def get_syslog_alert_id_by_name(self, syslog_alert_name: str):
        '''
        helper function to retrieve syslog alert object id by name
        :param syslog_alert_name: name of syslog alert object
        :return: syslogalert id if syslog alert is found, None otherwise
        '''
        syslogalerts = self.get_syslogalerts()
        for syslog_alert in syslogalerts:
            if syslog_alert['name'] == syslog_alert_name:
                return syslog_alert['id']
        return None

    def get_snmp_alert_id_by_name(self, snmp_alert_name: str):
        '''
        helper function to retrieve snmp alert object id by name
        :param snmp_alert_name: name of snmp alert object
        :return: snmpalert id if snmp alert is found, None otherwise
        '''
        snmp_alerts = self.get_snmpalerts()
        for snmp_alert in snmp_alerts:
            if snmp_alert['name'] == snmp_alert_name:
                return snmp_alert['id']
        return None

    def get_domain_id_by_name(self, domain_name: str):
        '''
        helper function to retrieve domain id from list of domains
        :param domain_name: name of the domain
        :return: did if domain is found, None otherwise
        '''
        for domain in self.domains:
            if domain['name'] == domain_name:
                return domain['uuid']
        self.logger.error(f'Could not find domain with name {domain_name}. Make sure full path is provided')
        available_domains = ', '.join((domain['name'] for domain in self.domains))
        self.logger.debug(f'Available Domains: {available_domains}')
        return None

    def get_domain_name_by_id(self, domain_id: str):
        '''
        helper function to retrieve domain name by id
        :param domain_id: id of the domain
        :return: name if domain is found, None otherwise
        '''
        for domain in self.domains:
            if domain['uuid'] == domain_id:
                return domain['name']
        self.logger.error(f'Could not find domain with id {domain_id}. Make sure full path is provided')
        available_domains = ', '.join((domain['uuid'] for domain in self.domains))
        self.logger.debug(f'Available Domains: {available_domains}')
        return None

    def get_system_version(self):
        request = '/info/serverversion'
        url = self._url('platform', request)
        return self._get(url)

    def get_audit_records(self):
        request = '/audit/auditrecords'
        url = self._url('platform', request)
        return self._get(url)

    def get_syslogalerts(self):
        request = '/policy/syslogalerts'
        url = self._url('config', request)
        return self._get(url)

    def get_snmpalerts(self):
        request = '/policy/snmpalerts'
        url = self._url('config', request)
        return self._get(url)

    def create_object(self, object_type: str, data: Dict):
        request = f'/object/{object_type}'
        url = self._url('config', request)
        return self._post(url, data)

    def get_objects(self, object_type: str, expanded=API_EXPANSION_MODE):
        request = f'/object/{object_type}'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_objects_override(self, objects: List, object_type: str, expanded=API_EXPANSION_MODE):
        overrides = list()
        for obj in objects:
            if obj['overridable']:
                responses = self.get_object_override(object_type, obj['id'], expanded=expanded)
                overrides.extend(responses)
        return overrides

    def get_object(self, object_type: str, object_id: str):
        request = f'/object/{object_type}/{object_id}'
        url = self._url('config', request)
        return self._get(url)

    def get_object_override(self, object_type: str, object_id: str, expanded=API_EXPANSION_MODE):
        request = f'/object/{object_type}/{object_id}/overrides'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def update_object(self, object_type: str, object_id: str, data: Dict):
        request = f'/object/{object_type}/{object_id}'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_object(self, object_type: str, object_id: str):
        request = f'/object/{object_type}/{object_id}'
        url = self._url('config', request)
        return self._delete(url)

    def create_device(self, data: Dict):
        request = '/devices/devicerecords'
        url = self._url('config', request)
        return self._post(url, data)

    def get_devices(self, expanded=API_EXPANSION_MODE):
        request = '/devices/devicerecords'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_device(self, device_id: str):
        request = f'/devices/devicerecords/{device_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_device(self, device_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_device(self, device_id: str):
        request = f'/devices/devicerecords/{device_id}'
        url = self._url('config', request)
        return self._delete(url)

    def get_device_hapairs(self, expanded=API_EXPANSION_MODE):
        request = '/devicehapairs/ftddevicehapairs'
        params = {
            'expanded': expanded,
        }
        url = self._url('config', request)
        return self._get(url, params)

    def create_device_hapair(self, data: Dict):
        request = '/devicehapairs/ftddevicehapairs/{}'
        url = self._url('config', request)
        return self._get(url, data)

    def get_device_hapair(self, device_hapair_id: str):
        request = f'/devicehapairs/ftddevicehapairs/{device_hapair_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_device_hapair(self, data: Dict, device_hapair_id: str):
        request = f'/devicehapairs/ftddevicehapairs/{device_hapair_id}'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_device_hapair(self, device_hapair_id: str):
        request = f'/devicehapairs/ftddevicehapairs/{device_hapair_id}'
        url = self._url('config', request)
        return self._delete(url)

    def get_device_hapair_monitoredinterfaces(self, device_hapair_id: str, expanded=API_EXPANSION_MODE):
        request = f'/devicehapairs/ftddevicehapairs/{device_hapair_id}/monitoredinterfaces'
        params = {
            'expanded': expanded,
        }
        url = self._url('config', request)
        return self._get(url, params)

    def get_device_hapair_monitoredinterface(self, device_hapair_id: str, monitoredinterface_id: str):
        request = f'/devicehapairs/ftddevicehapairs/{device_hapair_id}/monitoredinterfaces/{monitoredinterface_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_device_hapair_monitoredinterface(self, device_hapair_id: str, monitoredinterface_id: str, data: Dict):
        request = f'/devicehapairs/ftddevicehapairs/{device_hapair_id}/monitoredinterfaces/{monitoredinterface_id}'
        url = self._url('config', request)
        return self._put(url, data)

    def get_ftd_physical_interfaces(self, device_id: str, expanded=API_EXPANSION_MODE):
        request = f'/devices/devicerecords/{device_id}/physicalinterfaces'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_ftd_physical_interface(self, device_id: str, interface_id: str):
        request = f'/devices/devicerecords/{device_id}/physicalinterfaces/{interface_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_physical_interface(self, device_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/physicalinterfaces'
        url = self._url('config', request)
        return self._put(url, data)

    def create_ftd_redundant_interface(self, device_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/redundantinterfaces'
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_redundant_interfaces(self, device_id: str, expanded=API_EXPANSION_MODE):
        request = f'/devices/devicerecords/{device_id}/redundantinterfaces'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_ftd_redundant_interface(self, device_id: str, interface_id: str):
        request = f'/devices/devicerecords/{device_id}/redundantinterfaces/{interface_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_redundant_interface(self, device_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/redundantinterfaces'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_redundant_interface(self, device_id: str, interface_id: str):
        request = f'/devices/devicerecords/{device_id}/redundantinterfaces/{interface_id}'
        url = self._url('config', request)
        return self._delete(url)

    def create_ftd_portchannel_interface(self, device_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/etherchannelinterfaces'
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_portchannel_interfaces(self, device_id: str, expanded=API_EXPANSION_MODE):
        request = f'/devices/devicerecords/{device_id}/etherchannelinterfaces'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_ftd_portchannel_interface(self, device_id: str, interface_id: str):
        request = f'/devices/devicerecords/{device_id}/etherchannelinterfaces/{interface_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_portchannel_interface(self, device_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/etherchannelinterfaces'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_portchannel_interface(self, device_id: str, interface_id: str):
        request = f'/devices/devicerecords/{device_id}/etherchannelinterfaces/{interface_id}'
        url = self._url('config', request)
        return self._delete(url)

    def create_ftd_sub_interface(self, device_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/subinterfaces'
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_sub_interfaces(self, device_id: str, expanded=API_EXPANSION_MODE):
        request = f'/devices/devicerecords/{device_id}/subinterfaces'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_ftd_sub_interface(self, device_id: str, interface_id: str):
        request = f'/devices/devicerecords/{device_id}/subinterfaces/{interface_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_sub_interface(self, device_id: str, interface_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/subinterfaces/{interface_id}'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_sub_interface(self, device_id: str, interface_id: str):
        request = f'/devices/devicerecords/{device_id}/subinterfaces/{interface_id}'
        url = self._url('config', request)
        return self._delete(url)

    def create_ftd_ipv4staticroute(self, device_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes'
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_ipv4staticroutes(self, device_id: str, expanded=API_EXPANSION_MODE):
        request = f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_ftd_ipv4staticroute(self, device_id: str, route_id: str):
        request = f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes/{route_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_ipv4staticroute(self, device_id: str, route_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes/{route_id}'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_ipv4staticroute(self, device_id: str, route_id: str):
        request = f'/devices/devicerecords/{device_id}/routing/ipv4staticroutes/{route_id}'
        url = self._url('config', request)
        return self._delete(url)

    def create_ftd_ipv6staticroute(self, device_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes'
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_ipv6staticroutes(self, device_id: str, expanded=API_EXPANSION_MODE):
        request = f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_ftd_ipv6staticroute(self, device_id: str, route_id: str):
        request = f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes/{route_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_ipv6staticroute(self, device_id: str, route_id: str, data: Dict):
        request = f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes/{route_id}'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_ipv6staticroute(self, device_id: str, route_id: str):
        request = f'/devices/devicerecords/{device_id}/routing/ipv6staticroutes/{route_id}'
        url = self._url('config', request)
        return self._delete(url)

    def deploy(self, data: Dict):
        request = '/deployment/deploymentrequests'
        url = self._url('config', request)
        return self._post(url, data)

    def get_deployable_devices(self, expanded=API_EXPANSION_MODE):
        request = '/deployment/deployabledevices'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def create_policy(self, policy_type: str, data: Dict):
        request = f'/policy/{policy_type}'
        url = self._url('config', request)
        return self._post(url, data)

    def get_policies(self, policy_type: str, expanded=API_EXPANSION_MODE):
        request = f'/policy/{policy_type}'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_policy(self, policy_id: str, policy_type: str, expanded=API_EXPANSION_MODE):
        request = f'/policy/{policy_type}/{policy_id}'
        params = {
            'expanded': expanded,
        }
        url = self._url('config', request)
        return self._get(url, params)

    def update_policy(self, policy_id: str, policy_type: str, data: Dict):
        request = f'/policy/{policy_type}/{policy_id}'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_policy(self, policy_id: str, policy_type: str):
        request = f'/policy/{policy_type}/{policy_id}'
        url = self._url('config', request)
        return self._delete(url)

    def create_acp_rule(self, policy_id: str, data: Dict, section=str(), category=str(),
                        insert_before=int(), insert_after=int()):
        request = f'/policy/accesspolicies/{policy_id}/accessrules'
        url = self._url('config', request)
        params = {
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after
        }
        return self._post(url, data, params)

    def create_acp_rules(self, policy_id: str, data: Dict, section=str(), category=str(),
                         insert_before=int(), insert_after=int()):
        request = f'/policy/accesspolicies/{policy_id}/accessrules'
        url = self._url('config', request)
        params = {
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after
        }
        return self._post(url, data, params)

    def get_acp_rule(self, policy_id: str, rule_id: str):
        request = f'/policy/accesspolicies/{policy_id}/accessrules/{rule_id}'
        url = self._url('config', request)
        return self._get(url)

    def get_acp_rules(self, policy_id: str, expanded=API_EXPANSION_MODE):
        request = f'/policy/accesspolicies/{policy_id}/accessrules'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def update_acp_rule(self, policy_id: str, rule_id: str, data: Dict):
        request = f'/policy/accesspolicies/{policy_id}/accessrules/{rule_id}'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_acp_rule(self, policy_id: str, rule_id: str):
        request = f'/policy/accesspolicies/{policy_id}/accessrules/{rule_id}'
        url = self._url('config', request)
        return self._delete(url)

    def create_autonat_rule(self, policy_id: str, data: Dict):
        request = f'/policy/ftdnatpolicies/{policy_id}/autonatrules'
        url = self._url('config', request)
        return self._post(url, data)

    def get_autonat_rule(self, policy_id: str, rule_id: str):
        request = f'/policy/ftdnatpolicies/{policy_id}/autonatrules/{rule_id}'
        url = self._url('config', request)
        return self._get(url)

    def get_autonat_rules(self, policy_id: str, expanded=API_EXPANSION_MODE):
        request = f'/policy/ftdnatpolicies/{policy_id}/autonatrules'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def update_autonat_rule(self, policy_id: str, data: Dict):
        request = f'/policy/ftdnatpolicies/{policy_id}/autonatrules'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_autonat_rule(self, policy_id: str, rule_id: str):
        request = f'/policy/ftdnatpolicies/{policy_id}/autonatrules/{rule_id}'
        url = self._url('config', request)
        return self._delete(url)

    def create_manualnat_rule(self, policy_id: str, data: Dict):
        request = f'/policy/ftdnatpolicies/{policy_id}/manualnatrules'
        url = self._url('config', request)
        return self._post(url, data)

    def get_manualnat_rule(self, policy_id: str, rule_id: str):
        request = f'/policy/ftdnatpolicies/{policy_id}/manualnatrules/{rule_id}'
        url = self._url('config', request)
        return self._get(url)

    def get_manualnat_rules(self, policy_id: str, expanded=API_EXPANSION_MODE):
        request = f'/policy/ftdnatpolicies/manualnatrules/{policy_id}'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def update_manualnat_rule(self, policy_id: str, data: Dict):
        request = f'/policy/ftdnatpolicies/{policy_id}/manualnatrules'
        url = self._url('config', request)
        return self._put(url, data)

    def delete_manualnat_rule(self, policy_id: str, rule_id: str):
        request = f'/policy/ftdnatpolicies/{policy_id}/manualnatrules/{rule_id}'
        url = self._url('config', request)
        return self._delete(url)

    def create_policy_assignment(self, data: Dict):
        request = '/assignment/policyassignments'
        url = self._url('config', request)
        return self._post(url, data)

    def get_policy_assignments(self, expanded=API_EXPANSION_MODE):
        request = '/assignment/policyassignments'
        url = self._url('config', request)
        params = {
            'expanded': expanded,
        }
        return self._get(url, params)

    def get_policy_assignment(self, policy_id: str):
        request = f'/assignment/policyassignments/{policy_id}'
        url = self._url('config', request)
        return self._get(url)

    def update_policy_assignment(self, policy_id: str, data: Dict):
        request = f'/assignment/policyassignments/{policy_id}'
        url = self._url('config', request)
        return self._put(url, data)
