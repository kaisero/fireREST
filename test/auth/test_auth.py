import pytest

# -*- coding: utf-8 -*-

from fireREST import Client
from fireREST.exceptions import AuthError, AuthRefreshError
from requests.auth import HTTPBasicAuth


@pytest.fixture
def api(constants):
    return Client(hostname=constants['hostname'], username=constants['username'], password=constants['password'])
    api.domains = dict()
    del api.headers['X-auth-access-token']
    del api.headers['X-auth-refresh-token']


def test_authentication(api):
    api._login()

    assert api.domains is not None
    assert 'X-auth-access-token' in api.headers
    assert 'X-auth-refresh-token' in api.headers


def test_authentication_with_incorrect_credentials(api):
    api.cred = HTTPBasicAuth('firerest', 'incorrect-password')
    with pytest.raises(AuthError):
        api._login()


def test_authentication_refresh_counter_after_successful_authentication(api):
    api._login()
    expected_counter = 0
    actual_counter = api.refresh_counter

    assert actual_counter == expected_counter


def test_authentication_refresh_counter_incrementing(api):
    counter_before_refresh = api.refresh_counter
    api._refresh()

    expected_counter = counter_before_refresh + 1
    actual_counter = api.refresh_counter

    assert actual_counter == expected_counter


def test_re_authentication(api):
    api.refresh_counter = 3
    api._refresh()

    expected_counter = 0
    actual_counter = api.refresh_counter

    assert actual_counter == expected_counter
