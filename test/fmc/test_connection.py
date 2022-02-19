# -*- coding: utf-8 -*-

import pytest


from fireREST.fmc import Connection
from fireREST import exceptions as exc
from requests.auth import HTTPBasicAuth


@pytest.fixture
def connection(constants):
    return Connection(
        hostname=constants['hostname'],
        username=constants['username'],
        password=constants['password'],
        domain=constants['domain']['name'],
    )


def test_authentication_with_correct_credentials(conn):
    conn.domains = None
    del conn.headers['X-auth-access-token']
    del conn.headers['X-auth-refresh-token']

    conn.login()

    assert conn.domains is not None
    assert 'X-auth-access-token' in conn.headers
    assert 'X-auth-refresh-token' in conn.headers


def test_authentication_with_correct_credentials_and_dry_run_enabled(conn):
    conn.domains = None
    conn.dry_run = True
    del conn.headers['X-auth-access-token']
    del conn.headers['X-auth-refresh-token']

    conn.login()

    assert conn.domains is not None
    assert 'X-auth-access-token' in conn.headers
    assert 'X-auth-refresh-token' in conn.headers


def test_authentication_with_incorrect_credentials(connection):
    connection.cred = HTTPBasicAuth('firerest', 'incorrect-password')
    with pytest.raises(exc.AuthError):
        connection.login()


def test_authentication_refresh_counter_after_successful_authentication(conn):
    expected_counter = 0

    conn.login()
    actual_counter = conn.refresh_counter

    assert actual_counter == expected_counter


def test_authentication_refresh_counter_incrementing(conn):
    counter_before_refresh = conn.refresh_counter
    conn.refresh()

    expected_counter = counter_before_refresh + 1
    actual_counter = conn.refresh_counter

    assert actual_counter == expected_counter


def test_re_authentication(conn):
    conn.refresh_counter = 3
    conn.refresh()

    expected_counter = 0
    actual_counter = conn.refresh_counter

    assert actual_counter == expected_counter


def test_re_authentication_with_dry_run_enabled(conn):
    conn.refresh_counter = 3
    conn.dry_run = True
    conn.refresh()

    expected_counter = 0
    actual_counter = conn.refresh_counter

    assert actual_counter == expected_counter


def test_get_domain_id_with_correct_name(conn):
    expected_result = conn.domain['id']
    actual_result = conn.get_domain_id(conn.domain['name'])

    assert expected_result == actual_result


def test_get_domain_id_with_incorrect_name(conn):
    with pytest.raises(exc.DomainNotFoundError):
        conn.get_domain_id('NON-EXISTING-DOMAIN')
