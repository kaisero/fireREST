# -*- coding: utf-8 -*-

import pytest

import fireREST.exceptions as exc

from requests.auth import HTTPBasicAuth

from fireREST.fmc import Resource
from fireREST.defaults import API_AUTH_URL, API_REFRESH_URL, API_PLATFORM_URL, API_CONFIG_URL


def test_initialization(fmc, constants):
    expected_hostname = constants['hostname']
    expected_cred = HTTPBasicAuth(constants['username'], constants['password'])
    expected_refresh_counter = 0
    expected_protocol = 'https'
    expected_verify_cert = False
    expected_timeout = 120
    expected_domain_name = constants['domain']['name']

    assert fmc.conn.hostname == expected_hostname
    assert fmc.conn.cred == expected_cred
    assert fmc.conn.refresh_counter == expected_refresh_counter
    assert fmc.conn.protocol == expected_protocol
    assert fmc.conn.verify_cert == expected_verify_cert
    assert fmc.conn.timeout == expected_timeout
    assert fmc.conn.domain['name'] == expected_domain_name
    assert fmc.conn.domain['id'] is not None
    assert fmc.conn.domains is not None


def test_default_url_with_trailing_slash(fmc):
    expected_url = f'{fmc.conn.protocol}://{fmc.conn.hostname}/test'
    actual_url = fmc._url(path='/test/', namespace='base')
    assert actual_url == expected_url


def test_default_url(fmc):
    expected_url = f'{fmc.conn.protocol}://{fmc.conn.hostname}/test'
    actual_url = fmc._url(path='/test', namespace='base')
    assert actual_url == expected_url


def test_config_url(fmc):
    expected_url = f'{fmc.conn.protocol}://{fmc.conn.hostname}{API_CONFIG_URL}/domain/{fmc.conn.domain["id"]}/test'
    actual_url = fmc._url(path='/test', namespace='config')
    assert actual_url == expected_url


def test_platform_url(fmc):
    expected_url = f'{fmc.conn.protocol}://{fmc.conn.hostname}{API_PLATFORM_URL}/test'
    actual_url = fmc._url(path='/test', namespace='platform')
    assert actual_url == expected_url


def test_refresh_url(fmc):
    expected_url = f'{fmc.conn.protocol}://{fmc.conn.hostname}{API_REFRESH_URL}'
    actual_url = fmc._url(path='/test', namespace='refresh')
    assert actual_url == expected_url


def test_url_with_invalid_namespace(fmc):
    with pytest.raises(exc.InvalidNamespaceError):
        fmc._url(path='/test', namespace='nonExistingNamespace')
