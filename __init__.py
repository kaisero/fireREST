import json
import requests
import logging

from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

API_AUTH_URL = '/api/fmc_platform/v1/auth/generatetoken'
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
    def __init__(self, hostname=None, username=None, password=None, token=None,
                 protocol='https', verify_cert=False, logger=None, domain='Global', timeout=120):
        self.logger = self._get_logger(logger)
        self.hostname = hostname
        self.username = username
        self.password = password
        self.protocol = protocol
        self.verify_cert = verify_cert
        self.timeout = timeout
        self.cred = HTTPBasicAuth(self.username, self.password)
        if token is None:
            self._login()
        else:
            self.domains = token['domains']
            HEADERS['X-auth-access-token'] = token['token']
        self.domain = self.get_domain_id(domain)

    def _get_logger(self, logger):
        if not logger:
            dummy_logger = logging.getLogger('FireREST')
            dummy_logger.addHandler(logging.NullHandler())
            return dummy_logger
        return logger

    def _url(self, namespace='base', path=''):
        if namespace == 'config':
            return '{0}://{1}{2}/domain/{3}{4}'.format(self.protocol, self.hostname, API_CONFIG_URL, self.domain, path)
        if namespace == 'platform':
            return '{0}://{1}{2}{3}'.format(self.protocol, self.hostname, API_PLATFORM_URL, path)
        if namespace == 'auth':
            return '{0}://{1}{2}{3}'.format(self.protocol, self.hostname, API_AUTH_URL, path)
        return '{0}://{1}{2}'.format(self.protocol, self.hostname, path)

    def _login(self):
        try:
            request = self._url('auth')
            response = requests.post(request, headers=HEADERS, auth=self.cred, verify=self.verify_cert)

            if response.status_code == 401:
                raise FireRESTAuthException('FireREST API Authentication to {0} failed.'.format(self.hostname))

            token = response.headers.get('X-auth-access-token', default=None)
            if not token:
                raise FireRESTApiException('Could not retrieve token from {0}.'.format(request))

            HEADERS['X-auth-access-token'] = token
            self.domains = json.loads(response.headers.get('DOMAINS', default=None))
        except ConnectionError:
            self.logger.error(
                'Could not connect to {0}. Max retries exceeded with url: {1}'.format(self.hostname, request))
        except FireRESTApiException as exc:
            self.logger.error(exc.message)
        self.logger.debug('Successfully authenticated to {0}'.format(self.hostname))

    @RequestDebugDecorator('DELETE')
    def _delete(self, request, params=dict()):
        response = requests.delete(request, headers=HEADERS, params=params, verify=self.verify_cert,
                                   timeout=self.timeout)
        return response

    @RequestDebugDecorator('GET')
    def _get_request(self, request, params=dict(), limit=None):
        if limit:
            params['limit'] = limit
        response = requests.get(request, headers=HEADERS, params=params, verify=self.verify_cert,
                                timeout=self.timeout)
        return response

    def _get(self, request, params=dict(), limit=50):
        responses = list()
        response = self._get_request(request, params, limit)
        responses.append(response)
        payload = response.json()
        if 'paging' in payload.keys():
            pages = int(payload['paging']['pages'])
            for i in range(1, pages, 1):
                params['offset'] = str(int(i) * int(limit))
                response_page = self._get_request(request, params, limit)
                responses.append(response_page)
        return responses

    @RequestDebugDecorator('PATCH')
    def _patch(self, request, data=dict(), params=dict()):
        response = requests.patch(request, data=json.dumps(data), headers=HEADERS, params=params,
                                  verify=self.verify_cert, timeout=self.timeout)
        return response

    @RequestDebugDecorator('POST')
    def _post(self, request, data=dict(), params=dict()):
        response = requests.post(request, data=json.dumps(data), headers=HEADERS, params=params,
                                 verify=self.verify_cert, timeout=self.timeout)
        return response

    @RequestDebugDecorator('PUT')
    def _put(self, request, data=dict(), params=dict()):
        response = requests.put(request, data=json.dumps(data), headers=HEADERS, params=params,
                                verify=self.verify_cert, timeout=self.timeout)
        return response

    def get_object_id_by_name(self, obj_type, obj_name):
        request = '/object/{0}'.format(obj_type)
        url = self._url('config', request)
        response = self._get(url)
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == obj_name:
                    return payload['id']
        return None

    def get_device_id_by_name(self, device_name):
        request = '/devices/devicerecords'
        url = self._url('config', request)
        response = self._get(url)
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == device_name:
                    return payload['id']
        return None

    def get_acp_id_by_name(self, policy_name):
        request = '/policy/accesspolicies'
        url = self._url('config', request)
        response = self._get(url)
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == policy_name:
                    return payload['id']
        return None

    def get_rule_id_by_name(self, policy_name, rule_name):
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
        response = self.get_syslogalerts()
        for item in response:
            for payload in item.json()['items']:
                if payload['name'] == syslogalert_name:
                    return item['id']
        return None

    def get_domain_id(self, name):
        for domain in self.domains:
            if domain['name'] == name:
                return domain['uuid']
        logging.error('Could not find domain with name {0}. Make sure full path is provided'.format(name))
        logging.debug('Available Domains: {0}'.format(', '.join((domain['name'] for domain in self.domains))))
        return None

    def get_domain_name(self, id):
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
        url = self._url('config', request, limit=None)
        return self._get(url)

    def get_devices(self):
        request = '/devices/devicerecords'
        url = self._url('config', request)
        return self._get(url)

    def get_device(self, device_id):
        request = '/devices/devicerecords/{0}'.format(device_id)
        url = self._url('config', request, limit=None)
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
        url = self._url('config', request, limit=None)
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
        url = self._url('config', request, limit=None)
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
        request = 'policy/syslogalerts'
        url = self._url('config', request)
        return self._get(url)
