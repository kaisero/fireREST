import json
import requests
import logging
import urllib3

from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_AUTH_URL = '/api/fmc_platform/v1/auth/generatetoken'
API_REFRESH_URL = '/api/fmc_platform/v1/auth/refreshtoken'
API_PLATFORM_URL = '/api/fmc_platform/v1'
API_CONFIG_URL = '/api/fmc_config/v1'

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'fireREST'
}


class FireRESTApiException(Exception):
    pass


class FireRESTAuthException(Exception):
    pass


class FireRESTAuthRefreshException(Exception):
    pass


class RequestDebugDecorator(object):
    def __init__(self, action):
        self.action = action

    def __call__(self, f):
        def wrapped_f(*args):
            action = self.action
            logger = args[0].logger
            request = args[1]
            logger.debug('{0}: {1}'.format(action, request))
            result = f(*args)
            status_code = result.status_code
            logger.debug('Response Code: {0}'.format(status_code))
            if status_code >= 400:
                logger.debug('Error: {0}'.format(result.content))
            return result

        return wrapped_f


class FireREST(object):
    def __init__(self, hostname=None, username=None, password=None, session=None,
                 protocol='https', verify_cert=False, logger=None, domain='Global', timeout=120):
        """
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
        """
        self.refresh_counter = 0
        self.logger = self._get_logger(logger)
        self.hostname = hostname
        self.username = username
        self.password = password
        self.protocol = protocol
        self.verify_cert = verify_cert
        self.timeout = timeout
        self.cred = HTTPBasicAuth(self.username, self.password)
        if session is None:
            self._login()
        else:
            self.domains = session['domains']
            HEADERS['X-auth-access-token'] = session['X-auth-access-token']
            HEADERS['X-auth-refresh-token'] = session['X-auth-refresh-token']
        self.domain = self.get_domain_id(domain)

    @staticmethod
    def _get_logger(logger):
        """
        Generate dummy logger in case FireREST has been initialized without a logger
        :param logger: logger instance
        :return: dummy logger instance if logger is None, otherwise return logger variable again
        """
        if not logger:
            dummy_logger = logging.getLogger('FireREST')
            dummy_logger.addHandler(logging.NullHandler())
            return dummy_logger
        return logger

    def _url(self, namespace='base', path=''):
        """
        Generate URLs on the fly for requests to firepower api
        :param namespace: name of the url namespace that should be used. options: base, config, auth. default = base
        :param path: the url path for which a full url should be created
        :return: url in string format
        """
        if namespace == 'config':
            return '{0}://{1}{2}/domain/{3}{4}'.format(self.protocol, self.hostname, API_CONFIG_URL, self.domain, path)
        if namespace == 'platform':
            return '{0}://{1}{2}{3}'.format(self.protocol, self.hostname, API_PLATFORM_URL, path)
        if namespace == 'auth':
            return '{0}://{1}{2}{3}'.format(self.protocol, self.hostname, API_AUTH_URL, path)
        if namespace == 'refresh':
            return '{0}://{1}{2}{3}'.format(self.protocol, self.hostname, API_REFRESH_URL, path)
        return '{0}://{1}{2}'.format(self.protocol, self.hostname, path)

    def _login(self):
        """
        Login to fmc api and save X-auth-access-token, X-auth-refresh-token and DOMAINS to variables
        """
        try:
            request = self._url('auth')
            response = requests.post(request, headers=HEADERS, auth=self.cred, verify=self.verify_cert)

            if response.status_code == 401:
                raise FireRESTAuthException('FireREST API Authentication to {0} failed.'.format(self.hostname))

            access_token = response.headers.get('X-auth-access-token', default=None)
            refresh_token = response.headers.get('X-auth-refresh-token', default=None)
            if not access_token or not refresh_token:
                raise FireRESTApiException('Could not retrieve tokens from {0}.'.format(request))

            HEADERS['X-auth-access-token'] = access_token
            HEADERS['X-auth-refresh-token'] = refresh_token
            self.domains = json.loads(response.headers.get('DOMAINS', default=None))
        except ConnectionError:
            self.logger.error(
                'Could not connect to {0}. Max retries exceeded with url: {1}'.format(self.hostname, request))
        except FireRESTApiException as exc:
            self.logger.error(exc.message)
        self.logger.debug('Successfully authenticated to {0}'.format(self.hostname))

    def _refresh(self):
        """
        Refresh X-auth-access-token using X-auth-refresh-token- This operation is performed for up to three
        times, afterwards a re-authentication using _login will be performed
        """
        if self.refresh_counter > 3:
            self.logger.info(
                'Authentication token has already been used 3 times, api re-authentication will be performed')
            self._login()
        try:
            self.refresh_counter += 1
            request = self._url('refresh')
            response = requests.post(request, headers=HEADERS, verify=self.verify_cert)

            access_token = response.headers.get('X-auth-access-token', default=None)
            refresh_token = response.headers.get('X-auth-refresh-token', default=None)
            if not access_token or not refresh_token:
                raise FireRESTAuthRefreshException('Could not refresh tokens from {0}.'.format(request))

            HEADERS['X-auth-access-token'] = access_token
            HEADERS['X-auth-refresh-token'] = refresh_token
        except ConnectionError:
            self.logger.error(
                'Could not connect to {0}. Max retries exceeded with url: {1}'.format(self.hostname, request))
        except FireRESTApiException as exc:
            self.logger.error(exc.message)
        self.logger.debug('Successfully refreshed authorization token for {0}'.format(self.hostname))

    @RequestDebugDecorator('DELETE')
    def _delete(self, request, params=dict()):
        """
        DELETE Operation for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param params: dict of parameters for http request
        :return: requests.Response object
        """
        response = requests.delete(request, headers=HEADERS, params=params, verify=self.verify_cert,
                                   timeout=self.timeout)
        if response.status_code == 401:
            if 'Access token invalid' in str(response.json()):
                self._refresh()
                return self._delete(request, params)
        return response

    @RequestDebugDecorator('GET')
    def _get_request(self, request, params=dict(), limit=None):
        """
        GET Operation for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param params: dict of parameters for http request
        :param limit: set custom limit for paging. If not set, api will default to 25
        :return: requests.Response object
        """
        if limit:
            params['limit'] = limit
        response = requests.get(request, headers=HEADERS, params=params, verify=self.verify_cert,
                                timeout=self.timeout)
        if response.status_code == 401:
            if 'Access token invalid' in str(response.json()):
                self._refresh()
                return self._get_request(request, params, limit)
        return response

    def _get(self, request, params=dict(), limit=None):
        """
        GET Operation that supports paging for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param params: dict of parameters for http request
        :param limit: set custom limit for paging. If not set, api will default to 25
        :return: list of requests.Response objects
        """
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
    def _patch(self, request, data=dict(), params=dict()):
        """
        PATCH Operation for FMC REST API. In case of authentication issues session will be refreshed
        As of FPR 6.2.3 this function is not in use because FMC API does not support PATCH operations
        :param request: URL of request that should be performed
        :param data: dictionary of data that will be sent to the api
        :param params: dict of parameters for http request
        :return: requests.Response object
        """
        response = requests.patch(request, data=json.dumps(data), headers=HEADERS, params=params,
                                  verify=self.verify_cert, timeout=self.timeout)
        if response.status_code == 401:
            if 'Access token invalid' in str(response.json()):
                self._refresh()
                return self._patch(request, data, params)
        return response

    @RequestDebugDecorator('POST')
    def _post(self, request, data=dict(), params=dict()):
        """
        POST Operation for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param data: dictionary of data that will be sent to the api
        :param params: dict of parameters for http request
        :return: requests.Response object
        """
        response = requests.post(request, data=json.dumps(data), headers=HEADERS, params=params,
                                 verify=self.verify_cert, timeout=self.timeout)
        if response.status_code == 401:
            if 'Access token invalid' in str(response.json()):
                self._refresh()
                return self._post(request, data, params)
        return response

    @RequestDebugDecorator('PUT')
    def _put(self, request, data=dict(), params=dict()):
        """
        PUT Operation for FMC REST API. In case of authentication issues session will be refreshed
        :param request: URL of request that should be performed
        :param data: dictionary of data that will be sent to the api
        :param params: dict of parameters for http request
        :return: requests.Response object
        """
        response = requests.put(request, data=json.dumps(data), headers=HEADERS, params=params,
                                verify=self.verify_cert, timeout=self.timeout)
        if response.status_code == 401:
            if 'Access token invalid' in str(response.json()):
                self._refresh()
                return self._put(request, data, params)
        return response

    def get_object_id_by_name(self, obj_type, obj_name):
        """
        helper function to retrieve object id by name
        :param obj_type: object types that will be queried
        :param obj_name:  name of the object
        :return: id if object is found, None otherwise
        """
        request = '/object/{0}'.format(obj_type)
        url = self._url('config', request)
        response = self._get(url)
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == obj_name:
                    return payload['id']
        return None

    def get_device_id_by_name(self, device_name):
        """
        helper function to retrieve device id by name
        :param device_name:  name of the device
        :return: id if device is found, None otherwise
        """
        request = '/devices/devicerecords'
        url = self._url('config', request)
        response = self._get(url)
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == device_name:
                    return payload['id']
        return None

    def get_acp_id_by_name(self, policy_name):
        """
        helper function to retrieve access control policy id by name
        :param policy_name:  name of the access control policy
        :return: id if access control policy is found, None otherwise
        """
        request = '/policy/accesspolicies'
        url = self._url('config', request)
        response = self._get(url)
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == policy_name:
                    return payload['id']
        return None

    def get_rule_id_by_name(self, policy_name, rule_name):
        """
        helper function to retrieve access control policy rule id by name
        :param policy_name: name of the access control policy that will be queried
        :param rule_name:  name of the access control policy rule
        :return: id if access control policy rule is found, None otherwise
        """
        policy_id = self.get_acp_id_by_name(policy_name)
        request = '/policy/accesspolicies/{0}/accessrules'.format(policy_id)
        url = self._url('config', request)
        response = self._get(url)
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == rule_name:
                    return payload['id']
        return None

    def get_syslogalert_id_by_name(self, syslogalert_name):
        """
        helper function to retrieve syslog alert object id by name
        :param syslogalert_name: name of syslog alert object
        :return: id if syslog alert is found, None otherwise
        """
        # response = self.get_syslogalerts()
        request = '/policy/syslogalerts'
        url = self._url('config', request)
        response = self._get(url)

        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == syslogalert_name:
                    return payload['id']
        return None

    def get_domain_id(self, name):
        """
        helper function to retrieve domain id from list of domains
        :param name: name of the domain
        :return: did if domain is found, None otherwise
        """
        for domain in self.domains:
            if domain['name'] == name:
                return domain['uuid']
        logging.error('Could not find domain with name {0}. Make sure full path is provided'.format(name))
        logging.debug('Available Domains: {0}'.format(', '.join((domain['name'] for domain in self.domains))))
        return None

    def get_domain_name(self, id):
        """
        helper function to retrieve domain name by id
        :param id: id of the domain
        :return: name if domain is found, None otherwise
        """
        for domain in self.domains:
            if domain['uuid'] == id:
                return domain['name']
        logging.error('Could not find domain with id {0}. Make sure full path is provided'.format(id))
        logging.debug('Available Domains: {0}'.format(', '.join((domain['uuid'] for domain in self.domains))))
        return None

    def get_system_version(self):
        request = '/info/serverversion'
        url = self._url('platform', request)
        return self._get(url)

    def get_audit_records(self):
        request = '/audit/auditrecords'
        url = self._url('platform', request)
        return self._get(url)

    def create_object(self, object_type, data):
        request = '/object/{0}'.format(object_type)
        url = self._url('config', request)
        return self._post(url, data)

    def delete_object(self, object_type, object_id):
        request = '/object/{0}/{1}'.format(object_type, object_id)
        url = self._url('config', request)
        return self._delete(url)

    def update_object(self, object_type, object_id, data):
        request = '/object/{0}/{1}'.format(object_type, object_id)
        url = self._url('config', request)
        return self._put(url, data)

    def get_objects(self, object_type, expanded=False):
        request = '/object/{0}'.format(object_type)
        url = self._url('config', request)
        params = {
            'expanded': expanded
        }
        return self._get(url, params)

    def get_object(self, object_type, object_id):
        request = '/object/{0}/{1}'.format(object_type, object_id)
        url = self._url('config', request)
        return self._get(url)

    def get_devices(self):
        request = '/devices/devicerecords'
        url = self._url('config', request)
        return self._get(url)

    def get_device(self, device_id):
        request = '/devices/devicerecords/{0}'.format(device_id)
        url = self._url('config', request)
        return self._get(url)

    def get_deployment(self):
        request = '/deployment/deployabledevices'
        url = self._url('config', request)
        return self._get(url)

    def set_deployment(self, data):
        request = '/deployment/deployabledevices'
        url = self._url('config', request)
        return self._post(url, data)

    def create_policy(self, policy_type, data):
        request = '/policy/{0}'.format(policy_type)
        url = self._url('config', request)
        return self._post(url, data)

    def delete_policy(self, policy_id, policy_type):
        request = '/policy/{0}/{1}'.format(policy_type, policy_id)
        url = self._url('config', request)
        return self._delete(url)

    def update_policy(self, policy_id, policy_type, data):
        request = '/policy/{0}/{1}'.format(policy_type, policy_id)
        url = self._url('config', request)
        return self._put(url, data)

    def get_policies(self, policy_type):
        request = '/policy/{0}'.format(policy_type)
        url = self._url('config', request)
        return self._get(url)

    def get_policy(self, policy_id, policy_type, expanded=False):
        request = '/policy/{0}/{1}'.format(policy_type, policy_id)
        params = {
            'expanded': expanded
        }
        url = self._url('config', request)
        return self._get(url, params)

    def get_acp_rules(self, policy_id, expanded=False):
        request = '/policy/accesspolicies/{0}/accessrules'.format(policy_id)
        params = {
            'expanded': expanded
        }
        url = self._url('config', request)
        return self._get(url, params)

    def get_acp_rule(self, policy_id, rule_id):
        request = '/policy/accesspolicies/{0}/accessrules/{1}'.format(policy_id, rule_id)
        url = self._url('config', request)
        return self._get(url)

    def create_acp_rule(self, policy_id, data):
        request = '/policy/accesspolicies/{0}/accessrules'.format(policy_id)
        url = self._url('config', request)
        return self._post(url, data)

    def create_acp_rules(self, policy_id, data, section=None, category=None, insert_before=None, insert_after=None):
        request = '/policy/accesspolicies/{0}/accessrules'.format(policy_id)
        url = self._url('config', request)
        params = {
            'category': category,
            'section': section,
            'insert_before': insert_before,
            'insert_after': insert_after
        }
        return self._post(url, data, params)

    def update_acp_rule(self, policy_id, rule_id, data):
        request = '/policy/accesspolicies/{0}/accessrules/{1}'.format(policy_id, rule_id)
        url = self._url('config', request)
        return self._put(url, data)

    def get_syslogalerts(self):
        request = '/policy/syslogalerts'
        url = self._url('config', request)
        return self._get(url)

    def get_intrusion_policies(self):
        request = '/policy/intrusionpolicies'
        url = self._url('config', request)
        return self._get(url)

    def get_intrusion_policy_id_by_name(self, intrusion_policy_name):
        """
        helper function to retrieve intrusion policy object id by name
        :param intrusion_policy_name: name of intrusion policy object
        :return: id if intrusion policy is found, None otherwise
        """
        response = self.get_intrusion_policies()
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == intrusion_policy_name:
                    return payload['id']
        return None

    def get_variable_sets(self):
        request = '/object/variablesets'
        url = self._url('config', request)
        return self._get(url)

    def get_variable_set_id_by_name(self, variable_set_name):
        """
        helper function to retrieve variable set object id by name
        :param variable_set_name: name of variable set object
        :return: id if variable set is found, None otherwise
        """
        response = self.get_variable_sets()
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == variable_set_name:
                    return payload['id']
        return None

    def get_file_policies(self):
        request = '/policy/filepolicies'
        url = self._url('config', request)
        return self._get(url)

    def get_file_policy_id_by_name(self, file_policy_name):
        """
        helper function to retrieve file policy object id by name
        :param file_policy_name: name of file policy object
        :return: id if file policy is found, None otherwise
        """
        response = self.get_file_policies()
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == file_policy_name:
                    return payload['id']
        return None

