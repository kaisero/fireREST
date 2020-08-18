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


def test_get_domain_id_by_name_with_correct_name(api):
    expected_result = api.domain
    actual_result = api.get_domain_id_by_name(api.domain_name)

    assert expected_result == actual_result


def test_get_domain_id_by_name_with_incorrect_name(api):
    expected_result = None
    actual_result = api.get_domain_id_by_name('NON-EXISTING-DOMAIN')

    assert expected_result == actual_result


def test_get_domain_name_by_id_with_correct_id(api):
    expected_result = 'Global'
    actual_result = api.get_domain_name_by_id(api.domain)

    assert expected_result == actual_result


def test_get_domain_name_by_id_with_incorrect_id(api):
    expected_result = None
    actual_result = api.get_domain_name_by_id('NON-EXISTING-DOMAIN-ID')

    assert expected_result == actual_result


def test_create_object(api):
    payload = {
        'name': 'firerest_test_netobj',
        'value': '198.18.0.0/24',
    }

    actual_result = api.create_object('network', payload).status_code
    expected_result = 201

    assert expected_result == actual_result


def test_get_object(api):
    object_id = api.get_object_id_by_name('network', 'firerest_test_netobj')
    expected_object = {
        'id': object_id,
        'name': 'firerest_test_netobj',
        'value': '198.18.0.0/24',
    }
    actual_object = api.get_object('network', object_id)

    assert expected_object['id'] == actual_object['id']
    assert expected_object['name'] == actual_object['name']
    assert expected_object['value'] == actual_object['value']


def test_update_object(api):
    expected_response = 200
    expected_description = 'test_update_object'

    object_id = api.get_object_id_by_name('network', 'firerest_test_netobj')
    payload = api.get_object('network', object_id)
    payload['description'] = expected_description

    actual_response = api.update_object('network', object_id, payload).status_code
    actual_description = api.get_object('network', object_id)['description']

    assert expected_response == actual_response
    assert expected_description == actual_description


def test_delete_object(api):
    object_id = api.get_object_id_by_name('network', 'firerest_test_netobj')

    actual_result = api.delete_object('network', object_id).status_code
    expected_result = 200

    assert expected_result == actual_result
