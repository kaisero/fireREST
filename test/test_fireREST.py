# -*- coding: utf-8 -*-

import pytest

from fireREST import Client
from requests.auth import HTTPBasicAuth


def test_initialization(api, constants):
    expected_hostname = constants['hostname']
    expected_cred = HTTPBasicAuth(constants['username'], constants['password'])
    expected_refresh_counter = 0
    expected_protocol = 'https'
    expected_verify_cert = False
    expected_timeout = 120
    expected_domain_name = 'Global'

    assert api.hostname == expected_hostname
    assert api.cred == expected_cred
    assert api.refresh_counter == expected_refresh_counter
    assert api.protocol == expected_protocol
    assert api.verify_cert == expected_verify_cert
    assert api.timeout == expected_timeout
    assert api.domain_name == expected_domain_name