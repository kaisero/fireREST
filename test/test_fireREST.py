import unittest
import sys

sys.path.append('/home/okaiser/PycharmProjects/fireREST')

from copy import deepcopy
from fireREST import FireREST
from fireREST import FireRESTApiException, FireRESTAuthException, FireRESTAuthRefreshException
from requests.auth import HTTPBasicAuth


class TestFireREST(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestFireREST, cls).setUpClass()
        cls.hostname = 'fmc.example.com'
        cls.username = 'admin'
        cls.password = 'Cisco123'

        cls.api = FireREST(hostname=cls.hostname,
                           username=cls.username,
                           password=cls.password)

    def setUp(self):
        self.api_copy = deepcopy(self.api)

    def tearDown(self):
        return

    def test_initialization(self):
        expected_hostname = self.hostname
        expected_cred = HTTPBasicAuth(self.username, self.password)
        expected_refresh_counter = 0
        expected_protocol = 'https'
        expected_verify_cert = False
        expected_timeout = 120
        expected_domain = self.api.get_domain_id_by_name('Global')

        self.assertEqual(self.api.hostname, expected_hostname)
        self.assertEqual(self.api.cred, expected_cred)
        self.assertEqual(self.api.refresh_counter, expected_refresh_counter)
        self.assertEqual(self.api.protocol, expected_protocol)
        self.assertEqual(self.api.verify_cert, expected_verify_cert)
        self.assertEqual(self.api.timeout, expected_timeout)
        self.assertEqual(self.api.domain, expected_domain)

    def test_default_url(self):
        expected_url = '{}://{}{}'.format(self.api.protocol,
                                          self.api.hostname, '/test')
        actual_url = self.api._url(path='/test')

        self.assertEqual(actual_url, expected_url)

    def test_config_url(self):
        expected_url = '{}://{}{}/domain/{}{}'.format(self.api.protocol, self.api.hostname, FireREST.API_CONFIG_URL,
                                                      self.api.domain, '/test')
        actual_url = self.api._url(namespace='config', path='/test')

        self.assertEqual(actual_url, expected_url)

    def test_platform_url(self):
        expected_url = '{}://{}{}{}'.format(self.api.protocol,
                                            self.api.hostname, FireREST.API_PLATFORM_URL, '/test')
        actual_url = self.api._url(namespace='platform', path='/test')

        self.assertEqual(actual_url, expected_url)

    def test_auth_url(self):
        expected_url = '{}://{}{}'.format(self.api.protocol,
                                          self.api.hostname, FireREST.API_AUTH_URL)
        actual_url = self.api._url(namespace='auth')

        self.assertEqual(actual_url, expected_url)

    def test_refresh_url(self):
        expected_url = '{}://{}{}'.format(self.api.protocol,
                                          self.api.hostname, FireREST.API_REFRESH_URL)
        actual_url = self.api._url(namespace='refresh', path='/test')

        self.assertEqual(actual_url, expected_url)

    def test_authentication(self):
        self.api_copy.domains = dict()
        del self.api_copy.headers['X-auth-access-token']
        del self.api_copy.headers['X-auth-refresh-token']

        self.api_copy._login()

        self.assertTrue(self.api_copy.domains)
        self.assertIn('X-auth-access-token', self.api_copy.headers)
        self.assertIn('X-auth-refresh-token', self.api_copy.headers)

    def test_authentication_with_incorrect_credentials(self):
        self.api_copy.cred = HTTPBasicAuth('admin', 'incorrect-password')
        self.assertRaises(FireRESTAuthException, self.api_copy._login)

    def test_authentication_with_incorrect_destination(self):
        self.api_copy.hostname = '127.0.0.1'
        self.assertRaises(FireRESTApiException, self.api_copy._login)

    def test_refresh(self):
        return

    def test_authentication_triggered_by_refresh(self):
        return


if __name__ == '__main__':
    unittest.main()
