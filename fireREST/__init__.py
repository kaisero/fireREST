import json
import requests
import logging
import urllib3

from time import sleep
from typing import Dict
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import ConnectionError


class FireRESTApiException(Exception):
    def __init__(self, message):
        super().__init__(message)


class FireRESTAuthException(Exception):
    def __init__(self, message):
        super().__init__(message)


class FireRESTAuthRefreshException(Exception):
    def __init__(self, message):
        super().__init__(message)


class FireRESTRateLimitException(Exception):
    def __init__(self, message):
        super().__init__(message)


class RequestDebugDecorator(object):
    def __init__(self, action):
        self.action = action

    def __call__(self, f):
        def wrapped_f(*args):
            action = self.action
            logger = args[0].logger
            request = args[1]
            logger.debug('{}: {}'.format(action, request))
            result = f(*args)
            status_code = result.status_code
            logger.debug('Response Code: {}'.format(status_code))
            if status_code >= 400:
                logger.debug('Error: {}'.format(result.content))
            return result

        return wrapped_f


class FireREST(object):
    API_AUTH_URL = '/api/fmc_platform/v1/auth/generatetoken'
    API_REFRESH_URL = '/api/fmc_platform/v1/auth/refreshtoken'
    API_PLATFORM_URL = '/api/fmc_platform/v1'
    API_CONFIG_URL = '/api/fmc_config/v1'

    def __init__(self, hostname=str(), username=str(), password=str(), session=dict(), protocol='https',
                 verify_cert=False, logger=None, domain='Global', timeout=120):
        '''
        Initialize FireREST object
        :param hostname: ip address or dns name of fmc
        :param username: fmc username
        :param password: fmc password
        :param session: authentication session (can be provided in case FireREST should not generate one at init).
                      Make sure to pass the headers of a successful authentication to the session variable,
                      otherwise this will fail
        :param protocol: protocol used to access fmc api. default = https
        :param verify_cert: check fmc certificate for vailidity. default = False
        :param logger: optional logger instance, in case debug logging is needed
        :param domain: name of the fmc domain. default = Global
        :param timeout: timeout value for http requests. default = 120
        '''
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'fireREST'
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
        self.domain = self.get_domain_id_by_name(domain)

    @staticmethod
    def _get_logger(logger: object):
        '''
        Generate dummy logger in case FireREST has been initialized without a logger
        :param logger: logger instance
        :return: dummy logger instance if logger is None, otherwise return logger variable again
        '''
        if not logger:
            dummy_logger = logging.getLogger('FireREST')
            dummy_logger.addHandler(logging.NullHandler())
            return dummy_logger
        return logger

    def _url(self, namespace='base', path=str()):
        '''
        Generate URLs on the fly for requests to firepower api
        :param namespace: name of the url namespace that should be used. options: base, config, auth. default = base
        :param path: the url path for which a full url should be created
        :return: url in string format
        '''
        if namespace == 'config':
            return '{}://{}{}/domain/{}{}'.format(self.protocol, self.hostname, self.API_CONFIG_URL, self.domain, path)
        if namespace == 'platform':
            return '{}://{}{}{}'.format(self.protocol, self.hostname, self.API_PLATFORM_URL, path)
        if namespace == 'auth':
            return '{}://{}{}'.format(self.protocol, self.hostname, self.API_AUTH_URL)
        if namespace == 'refresh':
            return '{}://{}{}'.format(self.protocol, self.hostname, self.API_REFRESH_URL)
        return '{}://{}{}'.format(self.protocol, self.hostname, path)

    def _login(self):
        '''
        Login to fmc api and save X-auth-access-token, X-auth-refresh-token and DOMAINS to variables
        '''
        request = self._url('auth')
        try:
            response = requests.post(request, headers=self.headers, auth=self.cred, verify=self.verify_cert)

            if response.status_code in (401, 403):
                self.logger.error('API Authentication to {} failed.'.format(self.hostname))
                raise FireRESTAuthException('API Authentication to {} failed.'.format(self.hostname))

            if response.status_code == 429:
                msg = 'API Authentication to {} failed due to FMC rate limiting. Backing off for 10 seconds.'\
                    .format(self.hostname)
                raise FireRESTRateLimitException(msg)

            access_token = response.headers.get('X-auth-access-token', default=None)
            refresh_token = response.headers.get('X-auth-refresh-token', default=None)
            if not access_token or not refresh_token:
                self.logger.error('Could not retrieve tokens from {}.'.format(request))
                raise FireRESTApiException('Could not retrieve tokens from {}.'.format(request))

            self.headers['X-auth-access-token'] = access_token
            self.headers['X-auth-refresh-token'] = refresh_token
            self.domains = json.loads(response.headers.get('DOMAINS', default=None))
            self.refresh_counter = 0
            self.logger.debug('Successfully authenticated to {}'.format(self.hostname))
        except ConnectionRefusedError:
            self.logger.error('Could not connect to {}. Connection refused'.format(self.hostname))
            raise
        except ConnectionError:
            self.logger.error('Could not connect to {}. Max retries exceeded with url: {}'
                              .format(self.hostname, request))
            raise
        except FireRESTRateLimitException:
            sleep(10)
            self._login()

    def _refresh(self):
        '''
        Refresh X-auth-access-token using X-auth-refresh-token. This operation is performed for up to three
        times, afterwards a re-authentication using _login will be performed
        '''
        if self.refresh_counter > 2:
            self.logger.info(
                'Authentication token has already been used 3 times, api re-authentication will be performed')
            self._login()
            return

        request = self._url('refresh')
        try:
            self.refresh_counter += 1
            response = requests.post(request, headers=self.headers, verify=self.verify_cert)

            if response.status_code == 429:
                msg = 'API Refresh to {} failed due to FMC rate limiting. Backing off for 10 seconds.'\
                    .format(self.hostname)
                raise FireRESTRateLimitException(msg)

            access_token = response.headers.get('X-auth-access-token', default=None)
            refresh_token = response.headers.get('X-auth-refresh-token', default=None)
            if not access_token or not refresh_token:
                raise FireRESTAuthRefreshException('Could not refresh tokens from {}. Response Code: {}'
                                                   .format(request, response.status_code))

            self.headers['X-auth-access-token'] = access_token
            self.headers['X-auth-refresh-token'] = refresh_token
        except ConnectionError:
            self.logger.error('Could not connect to {}. Max retries exceeded with url: {}'
                              .format(self.hostname, request))
        except FireRESTRateLimitException:
            sleep(10)
            self._login()
        except FireRESTApiException as exc:
            self.logger.error(str(exc))

        self.logger.debug('Successfully refreshed authorization token for {}'.format(self.hostname))

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
                msg = 'DELETE operation {} failed due to FMC rate limiting. Backing off for 10 seconds.'.format(request)
                raise FireRESTRateLimitException(msg)
        except FireRESTRateLimitException:
            sleep(10)
            return self._delete(request, params)
        return response

    @RequestDebugDecorator('GET')
    def _get_request(self, request: str, params=None, limit=25):
        '''
        GET Operation for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param params: dict of parameters for http request
        :param limit: set custom limit for paging. If not set, api will default to 25
        :return: requests.Response object
        '''
        if params is None:
            params = dict()
        params['limit'] = limit
        try:
            response = requests.get(request, headers=self.headers, params=params, verify=self.verify_cert,
                                    timeout=self.timeout)
            if response.status_code == 401:
                if 'Access token invalid' in str(response.json()):
                    self._refresh()
                    return self._get_request(request, params, limit)
            if response.status_code == 429:
                msg = 'GET operation {} failed due to FMC rate limiting. Backing off for 10 seconds.'.format(request)
                raise FireRESTRateLimitException(msg)
        except FireRESTRateLimitException:
            sleep(10)
            return self._get_request(request, params, limit)
        return response

    def _get(self, request: str, params=None, limit=25):
        '''
        GET Operation that supports paging for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param params: dict of parameters for http request
        :param limit: set custom limit for paging. If not set, api will default to 25
        :return: list of requests.Response objects
        '''
        if params is None:
            params = dict()
        responses = list()
        response = self._get_request(request, params, limit)
        responses.append(response)
        payload = response.json()
        if 'paging' in payload.keys():
            pages = int(payload['paging']['pages'])
            limit = int(payload['paging']['limit'])
            for i in range(1, pages, 1):
                params['offset'] = str(int(i) * limit)
                response_page = self._get_request(request, params, limit)
                responses.append(response_page)
        return responses

    @RequestDebugDecorator('PATCH')
    def _patch(self, request: str, data: Dict, params=None):
        '''
        PATCH Operation for FMC REST API. In case of authentication issues session will be refreshed
        As of FPR 6.2.3 this function is not in use because FMC API does not support PATCH operations
        :param request: URL of request that should be performed
        :param data: dictionary of data that will be sent to the api
        :param params: dict of parameters for http request
        :return: requests.Response object
        '''
        if params is None:
            params = dict()
        try:
            response = requests.patch(request, data=json.dumps(data), headers=self.headers, params=params,
                                      verify=self.verify_cert, timeout=self.timeout)
            if response.status_code == 401:
                if 'Access token invalid' in str(response.json()):
                    self._refresh()
                    return self._patch(request, data, params)
            if response.status_code == 429:
                msg = 'PATCH operation {} failed due to FMC rate limiting. Backing off for 10 seconds.'\
                    .format(request)
                raise FireRESTRateLimitException(msg)
        except FireRESTRateLimitException:
            sleep(10)
            return self._patch(request, data, params)
        return response

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
                msg = 'POST operation {} failed due to FMC rate limiting. Backing off for 10 seconds.'\
                    .format(request)
                raise FireRESTRateLimitException(msg)
        except FireRESTRateLimitException:
            sleep(10)
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
                msg = 'PUT operation {} failed due to FMC rate limiting. Backing off for 10 seconds.' \
                    .format(request)
                raise FireRESTRateLimitException(msg)
        except FireRESTRateLimitException:
            sleep(10)
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

    def valid_json(self, operation: str, obj_type: str, data: Dict):
        '''
        Validate json object to verify
        :param operation: PUT, POST
        :param obj_type: see supported types in schema.py
        :param data: json representing api object
        :return: dictionary containing results of json evaluation
        '''
        return

    def get_object_id_by_name(self, obj_type: str, obj_name: str):
        '''
        helper function to retrieve object id by name
        :param obj_type: object types that will be queried
        :param obj_name:  name of the object
        :return: object id if object is found, None otherwise
        '''
        request = '/object/{}'.format(obj_type)
        url = self._url('config', request)
        response = self._get(url)
        for item in response:
            for obj in item.json()['items']:
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
        response = self._get(url)
        for item in response:
            for device in item.json()['items']:
                if device['name'] == device_name:
                    return device['id']
        return None

    def get_device_hapair_id_by_name(self, device_hapair_name: str):
        '''
        heloer function to retrieve device ha-pair id by name
        :param device_hapair_name: name of the ha-pair
        :return: id if ha-pair is found, None otherwise
        '''
        request = 'devicehapairs/ftddevicehapairs'
        url = self._url(request)
        response = self._get(url)
        for item in response:
            for ha_pair in item.json()['items']:
                if ha_pair['name'] == device_hapair_name:
                    return ha_pair['id']
        return None

    def get_nat_policy_id_by_name(self, nat_policy_name: str):
        '''
        helper function to retrieve nat policy id by name
        :param nat_policy_name: name of nat policy
        :return: policy id if nat policy is found, None otherwise
        '''
        request = '/policy/ftdnatpolicies'
        url = self._url(request)
        response = self._get(url)
        for item in response:
            for nat_policy in item.json()['items']:
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
        response = self._get(url)
        for item in response:
            for acp in item.json()['items']:
                if acp['name'] == policy_name:
                    return acp['id']
        return None

    def get_acp_rule_id_by_name(self, policy_name: str, rule_name: str):
        '''
        helper function to retrieve access control policy rule id by name
        :param policy_name: name of the access control policy that will be queried
        :param rule_name:  name of the access control policy rule
        :return: acp rule id if access control policy rule is found, None otherwise
        '''
        policy_id = self.get_acp_id_by_name(policy_name)
        request = '/policy/accesspolicies/{}/accessrules'.format(policy_id)
        url = self._url('config', request)
        response = self._get(url)
        for item in response:
            for acp_rule in item.json()['items']:
                if acp_rule['name'] == rule_name:
                    return acp_rule['id']
        return None

    def get_syslog_alert_id_by_name(self, syslog_alert_name: str):
        '''
        helper function to retrieve syslog alert object id by name
        :param syslog_alert_name: name of syslog alert object
        :return: syslogalert id if syslog alert is found, None otherwise
        '''
        response = self.get_syslogalerts()
        for item in response:
            for syslog_alert in item.json()['items']:
                if syslog_alert['name'] == syslog_alert_name:
                    return syslog_alert['id']
        return None

    def get_snmp_alert_id_by_name(self, snmp_alert_name: str):
        '''
        helper function to retrieve snmp alert object id by name
        :param snmp_alert_name: name of snmp alert object
        :return: snmpalert id if snmp alert is found, None otherwise
        '''
        response = self.get_snmpalerts()
        for item in response:
            for snmp_alert in item.json()['items']:
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
        self.logger.error('Could not find domain with name {}. Make sure full path is provided'.format(domain_name))
        self.logger.debug('Available Domains: {}'.format(', '.join((domain['name'] for domain in self.domains))))
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
        self.logger.error('Could not find domain with id {}. Make sure full path is provided'.format(domain_id))
        self.logger.debug('Available Domains: {}'.format(', '.join((domain['uuid'] for domain in self.domains))))
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
        request = 'policy/syslogalerts'
        url = self._url('config', request)
        return self._get(url)

    def get_snmpalerts(self):
        request = 'policy/snmpalerts'
        url = self._url('config', request)
        return self._get(url)

    def create_object(self, object_type: str, data: Dict):
        request = '/object/{}'.format(object_type)
        url = self._url('config', request)
        return self._post(url, data)

    def get_objects(self, object_type: str, expanded=False):
        request = '/object/{}'.format(object_type)
        url = self._url('config', request)
        params = {
            'expanded': expanded
        }
        return self._get(url, params)

    def get_object(self, object_type: str, object_id: str):
        request = '/object/{}/{}'.format(object_type, object_id)
        url = self._url('config', request)
        return self._get(url)

    def update_object(self, object_type: str, object_id: str, data: Dict):
        request = '/object/{}/{}'.format(object_type, object_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_object(self, object_type: str, object_id: str):
        request = '/object/{}/{}'.format(object_type, object_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_device(self, data: Dict):
        request = '/devices/devicerecords'
        url = self._url('config', request)
        return self._post(url, data)

    def get_devices(self):
        request = '/devices/devicerecords'
        url = self._url('config', request)
        return self._get(url)

    def get_device(self, device_id: str):
        request = '/devices/devicerecords/{}'.format(device_id)
        url = self._url('config', request)
        return self._get(url)

    def update_device(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}'.format(device_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_device(self, device_id: str):
        request = '/devices/devicerecords/{}'.format(device_id)
        url = self._url('config', request)
        return self._delete(url)

    def get_device_hapairs(self):
        request = '/devicehapairs/ftddevicehapairs'
        url = self._url('config', request)
        return self._get(url)

    def create_device_hapair(self, data: Dict):
        request = '/devicehapairs/ftddevicehapairs/{}'
        url = self._url('config', request)
        return self._get(url, data)

    def get_device_hapair(self, device_hapair_id: str):
        request = '/devicehapairs/ftddevicehapairs/{}'.format(device_hapair_id)
        url = self._url('config', request)
        return self._get(url)

    def update_device_hapair(self, data: Dict, device_hapair_id: str):
        request = '/devicehapairs/ftddevicehapairs/{}'.format(device_hapair_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_device_hapair(self, device_hapair_id: str):
        request = '/devicehapairs/ftddevicehapairs/{}'.format(device_hapair_id)
        url = self._url('config', request)
        return self._delete(url)

    def get_ftd_physical_interfaces(self, device_id: str):
        request = '/devices/devicerecords/{}/physicalinterfaces'.format(
            device_id)
        url = self._url('config', request)
        return self._get(url)

    def get_ftd_physical_interface(self, device_id: str, interface_id: str):
        request = '/devices/devicerecords/{}/physicalinterfaces/{}'.format(device_id, interface_id)
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_physical_interface(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/physicalinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._put(url, data)

    def create_ftd_redundant_interface(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/redundantinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_redundant_interfaces(self, device_id: str):
        request = '/devices/devicerecords/{}/redundantinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._get(url)

    def get_ftd_redundant_interface(self, device_id: str, interface_id: str):
        request = '/devices/devicerecords/{}/redundantinterfaces/{}'.format(device_id, interface_id)
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_redundant_interface(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/redundantinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_redundant_interface(self, device_id: str, interface_id: str):
        request = '/devices/devicerecords/{}/redundantinterfaces/{}'.format(device_id, interface_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_ftd_portchannel_interface(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/etherchannelinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_portchannel_interfaces(self, device_id: str):
        request = '/devices/devicerecords/{}/etherchannelinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._get(url)

    def get_ftd_portchannel_interface(self, device_id: str, interface_id: str):
        request = '/devices/devicerecords/{}/etherchannelinterfaces/{}'.format(device_id, interface_id)
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_portchannel_interface(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/etherchannelinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_portchannel_interface(self, device_id: str, interface_id: str):
        request = '/devices/devicerecords/{}/etherchannelinterfaces/{}'.format(device_id, interface_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_ftd_sub_interface(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/subinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_sub_interfaces(self, device_id: str):
        request = '/devices/devicerecords/{}/subinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._get(url)

    def get_ftd_sub_interface(self, device_id: str, interface_id: str):
        request = '/devices/devicerecords/{}/subinterfaces/{}'.format(device_id, interface_id)
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_sub_interface(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/subinterfaces'.format(device_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_sub_interface(self, device_id: str, interface_id: str):
        request = '/devices/devicerecords/{}/subinterfaces/{}'.format(device_id, interface_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_ftd_ipv4_route(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/ipv4staticroutes'.format(device_id)
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_ipv4_routes(self, device_id: str):
        request = '/devices/devicerecords/{}/ipv4staticroutes'.format(device_id)
        url = self._url('config', request)
        return self._get(url)

    def get_ftd_ipv4_route(self, device_id: str, route_id: str):
        request = '/devices/devicerecords/{}/ipv4staticroutes/{}'.format(device_id, route_id)
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_ipv4_route(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/ipv4staticroutes'.format(device_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_ipv4_route(self, device_id: str, route_id: str):
        request = '/devices/devicerecords/{}/ipv4staticroutes/{}'.format(device_id, route_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_ftd_ipv6_route(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/ipv6staticroutes'.format(device_id)
        url = self._url('config', request)
        return self._post(url, data)

    def get_ftd_ipv6_routes(self, device_id: str):
        request = '/devices/devicerecords/{}/ipv6staticroutes'.format(device_id)
        url = self._url('config', request)
        return self._get(url)

    def get_ftd_ipv6_route(self, device_id: str, route_id: str):
        request = '/devices/devicerecords/{}/ipv6staticroutes/{}'.format(device_id, route_id)
        url = self._url('config', request)
        return self._get(url)

    def update_ftd_ipv6_route(self, device_id: str, data: Dict):
        request = '/devices/devicerecords/{}/ipv6staticroutes'.format(device_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_ftd_ipv6_route(self, device_id: str, route_id: str):
        request = '/devices/devicerecords/{}/ipv6staticroutes/{}'.format(device_id, route_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_deployment(self, data: Dict):
        request = '/deployment/deploymentrequests'
        url = self._url('config', request)
        return self._post(url, data)

    def get_deployment(self):
        request = '/deployment/deployabledevices'
        url = self._url('config', request)
        return self._get(url)

    def create_policy(self, policy_type: str, data: Dict):
        request = '/policy/{}'.format(policy_type)
        url = self._url('config', request)
        return self._post(url, data)

    def get_policies(self, policy_type: str):
        request = '/policy/{}'.format(policy_type)
        url = self._url('config', request)
        return self._get(url)

    def get_policy(self, policy_id: str, policy_type: str, expanded=False):
        request = '/policy/{}/{}'.format(policy_type, policy_id)
        params = {
            'expanded': expanded
        }
        url = self._url('config', request)
        return self._get(url, params)

    def update_policy(self, policy_id: str, policy_type: str, data: Dict):
        request = '/policy/{}/{}'.format(policy_type, policy_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_policy(self, policy_id: str, policy_type: str):
        request = '/policy/{}/{}'.format(policy_type, policy_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_acp_rule(self, policy_id: str, data: Dict, section=str(), category=str(),
                        insert_before=int(), insert_after=int()):
        request = '/policy/accesspolicies/{}/accessrules'.format(policy_id)
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
        request = '/policy/accesspolicies/{}/accessrules'.format(policy_id)
        url = self._url('config', request)
        params = {
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after
        }
        return self._post(url, data, params)

    def get_acp_rule(self, policy_id: str, rule_id: str):
        request = '/policy/accesspolicies/{}/accessrules/{}'.format(policy_id, rule_id)
        url = self._url('config', request)
        return self._get(url)

    def get_acp_rules(self, policy_id: str, expanded=False):
        request = '/policy/accesspolicies/{}/accessrules'.format(policy_id)
        params = {
            'expanded': expanded
        }
        url = self._url('config', request)
        return self._get(url, params)

    def update_acp_rule(self, policy_id: str, rule_id: str, data: Dict):
        request = '/policy/accesspolicies/{}/accessrules/{}'.format(policy_id, rule_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_acp_rule(self, policy_id: str, rule_id: str):
        request = '/policy/accesspolicies/{}/accessrules/{}'.format(policy_id, rule_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_autonat_rule(self, policy_id: str, data: Dict):
        request = '/policy/ftdnatpolicies/{}/autonatrules'.format(policy_id)
        url = self._url('config', request)
        return self._post(url, data)

    def get_autonat_rule(self, policy_id: str, rule_id: str):
        request = '/policy/ftdnatpolicies/{}/autonatrules/{}'.format(policy_id, rule_id)
        url = self._url('config', request)
        return self._get(url)

    def get_autonat_rules(self, policy_id: str):
        request = '/policy/ftdnatpolicies/{}/autonatrules'.format(policy_id)
        url = self._url('config', request)
        return self._get(url)

    def update_autonat_rule(self, policy_id: str, data: Dict):
        request = '/policy/ftdnatpolicies/{}/autonatrules'.format(policy_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_autonat_rule(self, policy_id: str, rule_id: str):
        request = '/policy/ftdnatpolicies/{}/autonatrules/{}'.format(policy_id, rule_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_manualnat_rule(self, policy_id: str, data: Dict):
        request = '/policy/ftdnatpolicies/{}/manualnatrules'.format(policy_id)
        url = self._url('config', request)
        return self._post(url, data)

    def get_manualnat_rule(self, policy_id: str, rule_id: str):
        request = '/policy/ftdnatpolicies/{}/manualnatrules/{}'.format(policy_id, rule_id)
        url = self._url('config', request)
        return self._get(url)

    def get_manualnat_rules(self, policy_id: str):
        request = '/policy/ftdnatpolicies/manualnatrules/{}'.format(policy_id)
        url = self._url('config', request)
        return self._get(url)

    def update_manualnat_rule(self, policy_id: str, data: Dict):
        request = '/policy/ftdnatpolicies/{}/manualnatrules'.format(policy_id)
        url = self._url('config', request)
        return self._put(url, data)

    def delete_manualnat_rule(self, policy_id: str, rule_id: str):
        request = '/policy/ftdnatpolicies/{}/manualnatrules/{}'.format(policy_id, rule_id)
        url = self._url('config', request)
        return self._delete(url)

    def create_policy_assignment(self, data: Dict):
        request = '/assignment/policyassignments'
        url = self._url('config', request)
        return self._post(url, data)

    def get_policy_assignments(self):
        request = '/assignment/policyassignments'
        url = self._url('config', request)
        return self._get(url)

    def get_policy_assignment(self, policy_id: str):
        request = '/assignment/policyassignments/{}'.format(policy_id)
        url = self._url('config', request)
        return self._get(url)

    def update_policy_assignment(self, policy_id: str, data: Dict):
        request = '/assignment/policyassignments/{}'.format(policy_id)
        url = self._url('config', request)
        return self._put(url, data)
