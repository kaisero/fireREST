import unittest

from fireREST import Client
from fireREST import FireRESTApiException, FireRESTAuthException, FireRESTAuthRefreshException
from fireREST import API_AUTH_URL, API_REFRESH_URL, API_PLATFORM_URL, API_CONFIG_URL
from requests.auth import HTTPBasicAuth


class TestFireRESTAuth(unittest.TestCase):

    def setUp(self):
        hostname = 'fmc.example.com'
        username = 'admin'
        password = 'Cisco123'
        self.api = Client(hostname=hostname, username=username, password=password)

    def tearDown(self):
        return

    def test_authentication(self):
        self.api.domains = dict()
        del self.api.headers['X-auth-access-token']
        del self.api.headers['X-auth-refresh-token']

        self.api._login()

        self.assertTrue(self.api.domains)
        self.assertIn('X-auth-access-token', self.api.headers)
        self.assertIn('X-auth-refresh-token', self.api.headers)

    def test_authentication_with_incorrect_credentials(self):
        self.api.cred = HTTPBasicAuth('admin', 'incorrect-password')
        self.assertRaises(FireRESTAuthException, self.api._login)

    def test_authentication_refresh_counter_after_successful_authentication(self):
        self.api._login()
        expected_counter = 0
        actual_counter = self.api.refresh_counter

        self.assertEqual(actual_counter, expected_counter)

    def test_authentication_refresh_counter_incrementing(self):
        counter_before_refresh = self.api.refresh_counter
        self.api._refresh()

        expected_counter = counter_before_refresh + 1
        actual_counter = self.api.refresh_counter

        self.assertEqual(actual_counter, expected_counter)

    def test_re_authentication(self):
        self.api.refresh_counter = 3
        self.api._refresh()

        expected_counter = 0
        actual_counter = self.api.refresh_counter

        self.assertEqual(actual_counter, expected_counter)


class TestFireREST(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestFireREST, cls).setUpClass()
        cls.hostname = 'fmc.example.com'
        cls.username = 'admin'
        cls.password = 'Cisco123'

        cls.api = Client(hostname=cls.hostname, username=cls.username, password=cls.password)

    def setUp(self):
        return

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
        expected_url = f'{self.api.protocol}://{self.api.hostname}/test'
        actual_url = self.api._url(path='/test')
        self.assertEqual(actual_url, expected_url)

    def test_config_url(self):
        expected_url = f'{self.api.protocol}://{self.api.hostname}{API_CONFIG_URL}/domain/{self.api.domain}/test'
        actual_url = self.api._url(namespace='config', path='/test')
        self.assertEqual(actual_url, expected_url)

    def test_platform_url(self):
        expected_url = f'{self.api.protocol}://{self.api.hostname}{API_PLATFORM_URL}/test'
        actual_url = self.api._url(namespace='platform', path='/test')
        self.assertEqual(actual_url, expected_url)

    def test_auth_url(self):
        expected_url = f'{self.api.protocol}://{self.api.hostname}{API_AUTH_URL}'
        actual_url = self.api._url(namespace='auth')
        self.assertEqual(actual_url, expected_url)

    def test_refresh_url(self):
        expected_url = f'{self.api.protocol}://{self.api.hostname}{API_REFRESH_URL}'
        actual_url = self.api._url(namespace='refresh', path='/test')
        self.assertEqual(actual_url, expected_url)


if __name__ == '__main__':
    unittest.main()
