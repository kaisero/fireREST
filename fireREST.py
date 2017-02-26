import json
import requests
import sys
import logging
from rainbow_logging_handler import RainbowLoggingHandler

from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

API_AUTH_URL = '/api/fmc_platform/v1/auth/generatetoken'
API_PLATFORM_REQ_URL = '/api/fmc_platform/v1/'
API_CONFIG_REQ_URL = '/api/fmc_config/v1/'

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'fireREST'
}


class FireREST(object):
    def __init__(self, device=None, username=None, password=None, verify_cert=False, timeout=120, loglevel=20):

        self.logger = logging.getLogger('FireREST')
        self.logger.setLevel(loglevel)
        formatter = logging.Formatter('%(asctime)s [%(name)s] [%(levelname)s] %(message)s')
        handler = RainbowLoggingHandler(sys.stderr, color_funcName=('black', 'yellow', True))
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.device = device
        self.username = username
        self.password = password
        self.verify_cert = verify_cert
        self.timeout = timeout
        self.cred = HTTPBasicAuth(self.username, self.password)
        self.api_platform_request_url = API_PLATFORM_REQ_URL
        self.api_config_request_url = API_CONFIG_REQ_URL
        self.headers = HEADERS
        self.url_policy = {
            'accesspolicy': 'accesspolicies',
            'filepolicy': 'filepolicies',
            'intrusionpolicy': 'intrusionpolicies',
            'snmpalert': 'snmpalerts',
            'syslogalert': 'syslogalerts'
        }

        try:
            request = requests.post('https://' + self.device + API_AUTH_URL, headers=HEADERS,
                                    auth=self.cred,
                                    verify=self.verify_cert)
            self.token = request.headers.get('X-auth-access-token', default=None)
            self.domains = json.loads(request.headers.get('DOMAINS', default=None))
            self.headers['X-auth-access-token'] = self.token
        except Exception as error:
            self.logger.error('Could not generate Authentication Token, check connection parameters')
            self.logger.error('Exception: %s ' % error.message)
            sys.exit()

    ######################################################################
    # General Functions
    ######################################################################
    def _delete(self, request):
        url = 'https://' + self.device + request
        data = requests.delete(url, headers=self.headers, verify=self.verify_cert, timeout=self.timeout)
        return data

    def _get(self, request, limit=50):
        responses = list()
        url = 'https://' + self.device + request
        if limit:
            if '?' in request:
                url += '&limit=' + str(limit)
            else:
                url += '?limit=' + str(limit)
        data = requests.get(url, headers=self.headers, verify=self.verify_cert, timeout=self.timeout)
        payload = data.json()
        responses.append(data)
        if data.status_code == 200 and 'paging' in payload.keys():
            pages = int(payload['paging']['pages'])
            for i in xrange(1, pages, 1):
                url_with_offset = url + '&offset=' + str(int(i) * int(limit))
                response_page = requests.get(url_with_offset, headers=self.headers, verify=self.verify_cert,
                                             timeout=self.timeout)
                responses.append(response_page)
        return responses

    def _patch(self, request, data):
        url = 'https://' + self.device + request
        data = requests.patch(url, data=json.dumps(data), headers=self.headers, verify=self.verify_cert,
                              timeout=self.timeout)
        return data

    def _post(self, request, data=False):
        url = 'https://' + self.device + request
        if data:
            data = requests.post(url, data=json.dumps(data), headers=self.headers, verify=self.verify_cert,
                                 timeout=self.timeout)
        else:
            data = requests.post(url, headers=self.headers, verify=self.verify_cert, timeout=self.timeout)
        return data

    def _put(self, request, data):
        url = 'https://' + self.device + request
        data = requests.put(url, data=json.dumps(data), headers=self.headers, verify=self.verify_cert,
                            timeout=self.timeout)
        return data

    ######################################################################
    # HELPER FUNCTIONS
    ######################################################################

    def get_object_id_by_name(self, object_type, name, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        obj_type = object_type.lower() + 's'
        data = self._get(self.api_config_request_url + domain_url + 'object/%s' % obj_type).json()
        for item in data['items']:
            if item['name'] == name:
                return item['id']
        return None

    def get_device_id_by_name(self, name, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        data = self._get(self.api_config_request_url + domain_url + 'devices/devicerecords').json()
        for item in data['items']:
            if item['name'] == name:
                return item['id']
        return None

    def get_acp_id_by_name(self, name, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        responses = self._get(self.api_config_request_url + domain_url + 'policy/accesspolicies')
        for response in responses:
            for item in response.json()['items']:
                if item['name'] == name:
                    return item['id']
        return None

    def get_rule_id_by_name(self, policy_name, rule_name, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        policy_id = self.get_acp_id_by_name(policy_name)
        data = self._get(
            self.api_config_request_url + domain_url + 'policy/accesspolicies/' + policy_id + '/accessrules').json()
        for item in data['items']:
            if item['name'] == rule_name:
                return item['id']
        return None

    def get_domain_id(self, name):
        for domain in self.domains:
            if domain['name'] == name:
                return domain['uuid']
        logging.warn('Could not find domain with name %s. Make sure full path is provided' % domain['name'])
        logging.debug('Available Domains: %s' % self.domains)

    def get_domain_url(self, domain_id):
        return 'domain/%s/' % domain_id

    ######################################################################
    # <SYSTEM>
    ######################################################################

    def get_system_version(self):
        request = self.api_platform_request_url + 'info/serverversion'
        return self._get(request)

    def get_audit_records(self, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self.api_platform_request_url + domain_url + 'audit/auditrecords'
        return self._get(request)

    ######################################################################
    # <OBJECTS>
    ######################################################################

    def create_object(self, object_type, data, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        obj_type = object_type.lower() + 's'
        request = self.api_config_request_url + domain_url + 'object/' + obj_type
        response = self._post(request, data)
        if response.status_code == 201:
            self.logger.info('Object %s of type %s successfully created' % (data['name'], object_type))
        else:
            if response.status_code == 400 and 'error' in response.json():
                if 'The object name already exists' in response.json()['error']['messages'][0]['description']:
                    self.logger.info('Import of Object %s skipped, Object already exists.' % data['name'])
            else:
                self.logger.error('Import of Object %s failed with Reason: %s' % (
                    data['name'], response.json()))
                self.logger.debug('Object Dump: %s' % data)
        return response

    def delete_object(self, object_type, object_id, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self.api_config_request_url + domain_url + 'object/' + object_type + '/' + object_id
        return self._delete(request)

    def update_object(self, object_type, object_id, data, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self.api_config_request_url + domain_url + 'object/' + object_type + '/' + object_id
        return self._put(request, data)

    def get_objects(self, object_type, expanded=False, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        obj_type = object_type.lower() + 's'
        request = self.api_config_request_url + domain_url + 'object/' + obj_type
        if expanded:
            request += '?expanded=True'
        return self._get(request)

    def get_object(self, object_type, object_id, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        obj_type = object_type.lower() + 's'
        request = self._get(self.api_config_request_url + domain_url + 'object/' + obj_type + '/' + object_id)
        return request

    ######################################################################
    # </OBJECTS>
    ######################################################################


    ######################################################################
    # <DEVICES>
    ######################################################################

    def get_devices(self, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self._get(self.api_config_request_url + domain_url + 'devices/devicerecords')
        return request

    def get_device(self, device_id, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self._get(self.api_config_request_url + domain_url + 'devices/devicerecords/' + device_id)
        return request

    ######################################################################
    # </DEVICES>
    ######################################################################

    ######################################################################
    # <DEPLOYMENT>
    ######################################################################

    def get_deploy_devices(self, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self._get(self.api_config_request_url + domain_url + 'deployment/deployabledevices')
        return request

    def deploy_configuration(self, data, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self._post(self.api_config_request_url + domain_url + 'deployment/deploymentrequests')
        return request

    ######################################################################
    # </DEPLOYMENT>
    ######################################################################

    ######################################################################
    # <POLICIES>
    ######################################################################

    def create_policy(self, policy_type, data, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        policy_type = self.url_policy['policy_type']
        request = self.api_config_request_url + domain_url + 'policy/' + policy_type + '/'
        return self._post(request, data)

    def delete_policy(self, policy_id, policy_type, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        policy_type = self.url_policy['policy_type']
        request = self.api_config_request_url + domain_url + 'policy/' + policy_type + '/' + policy_id
        return self._delete(request)

    def update_policy(self, policy_id, policy_type, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        policy_type = self.url_policy['policy_type']
        request = self.api_config_request_url + domain_url + 'policy/' + policy_type + '/' + policy_id
        return self._put(request)

    def get_policies(self, policy_type, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        policy_type = self.url_policy['policy_type']
        request = self._get(self.api_config_request_url + domain_url + 'policy/' + policy_type)
        return request

    def get_policy(self, policy_id, policy_type, expanded=False, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        policy_type = self.url_policy[policy_type]
        request = self._get(self.api_config_request_url + domain_url + 'policy/' + policy_type + '/' + policy_id)
        if expanded:
            request += '?expanded=True'
        return request

    def get_acp_rules(self, policy_id, expanded=False, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self.api_config_request_url + domain_url + 'policy/accesspolicies/' + policy_id + '/accessrules'
        if expanded:
            request += '?expanded=True'
        return self._get(request)

    def get_acp_rule(self, policy_id, rule_id, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self._get(
            self.api_config_request_url + domain_url + 'policy/accesspolicies/' + policy_id + '/accessrules/' + rule_id,
            limit=None)
        return request

    def update_acp_rule(self, policy_id, rule_id, data, domain='Global'):
        domain_url = self.get_domain_url(self.get_domain_id(domain))
        request = self._put(
            self.api_config_request_url + domain_url + 'policy/accesspolicies/' + policy_id + '/accessrules/' + rule_id,
            data)
        return request
