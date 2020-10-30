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
    expected_domain_name = constants['domain']

    assert api.hostname == expected_hostname
    assert api.cred == expected_cred
    assert api.refresh_counter == expected_refresh_counter
    assert api.protocol == expected_protocol
    assert api.verify_cert == expected_verify_cert
    assert api.timeout == expected_timeout
    assert api.domain_name == expected_domain_name


def test_get_domain_id_with_correct_name(api):
    expected_result = api.domain
    actual_result = api.get_domain_id(api.domain_name)

    assert expected_result == actual_result


def test_get_domain_id_with_incorrect_name(api):
    expected_result = None
    actual_result = api.get_domain_id('NON-EXISTING-DOMAIN')

    assert expected_result == actual_result


def test_get_domain_name_by_id_with_correct_id(api, constants):
    expected_result = constants['domain']
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
    object_id = api.get_object_id('network', 'firerest_test_netobj')
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

    object_id = api.get_object_id('network', 'firerest_test_netobj')
    payload = api.get_object('network', object_id)
    payload['description'] = expected_description

    actual_response = api.update_object('network', object_id, payload).status_code
    actual_description = api.get_object('network', object_id)['description']

    assert expected_response == actual_response
    assert expected_description == actual_description


def test_delete_object(api):
    object_id = api.get_object_id('network', 'firerest_test_netobj')

    actual_result = api.delete_object('network', object_id).status_code
    expected_result = 200

    assert expected_result == actual_result


def test_get_device_id_with_correct_name(api, constants):
    expected_result = constants['device_id']
    actual_result = api.get_device_id(constants['device'])

    assert expected_result == actual_result


def test_get_device_id_with_incorrect_name(api, constants):
    expected_result = None
    actual_result = api.get_device_id('INCORRECT-NAME')

    assert expected_result == actual_result


def test_get_devicehapair_id_with_correct_name(api, constants):
    expected_result = constants['devicehapair_id']
    actual_result = api.get_devicehapair_id(constants['devicehapair'])

    assert expected_result == actual_result


def test_get_devicehapair_id_with_incorrect_name(api, constants):
    expected_result = None
    actual_result = api.get_devicehapair_id('INCORRECT-NAME')

    assert expected_result == actual_result


def test_get_accesspolicy_id_with_correct_name(api, constants):
    expected_result = constants['accesspolicy_id']
    actual_result = api.get_accesspolicy_id(constants['accesspolicy'])

    assert expected_result == actual_result


def test_get_accesspolicy_id_with_incorrect_name(api, constants):
    expected_result = None
    actual_result = api.get_accesspolicy_id('INCORRECT-NAME')

    assert expected_result == actual_result


def test_get_prefilterpolicy_id_with_correct_name(api, constants):
    expected_result = constants['prefilterpolicy_id']
    actual_result = api.get_prefilterpolicy_id(constants['prefilterpolicy'])

    assert expected_result == actual_result


def test_get_prefilterpolicy_id_with_incorrect_name(api, constants):
    expected_result = None
    actual_result = api.get_prefilterpolicy_id('INCORRECT-NAME')

    assert expected_result == actual_result


def test_get_accesspolicy_rule_id_with_correct_name(api, constants):
    expected_result = constants['accessrule_id']
    actual_result = api.get_accesspolicy_rule_id(constants['accesspolicy_id'], constants['accessrule'])

    assert expected_result == actual_result


def test_get_accesspolicy_rule_id_with_incorrect_name(api, constants):
    expected_result = None
    actual_result = api.get_accesspolicy_rule_id(constants['accesspolicy_id'], 'INCORRECT-NAME')

    assert expected_result == actual_result


def test_get_natpolicy_id_with_correct_name(api, constants):
    expected_result = constants['natpolicy_id']
    actual_result = api.get_natpolicy_id(constants['natpolicy'])

    assert expected_result == actual_result


def test_get_natpolicy_id_with_incorrect_name(api, constants):
    expected_result = None
    actual_result = api.get_natpolicy_id('INCORRECT-NAME')

    assert expected_result == actual_result


def test_get_syslogalert_id_with_correct_name(api, constants):
    expected_result = constants['syslogalert_id']
    actual_result = api.get_syslogalert_id(constants['syslogalert'])

    assert expected_result == actual_result


def test_get_syslogalert_id_with_incorrect_name(api, constants):
    expected_result = None
    actual_result = api.get_syslogalert_id('INCORRECT-NAME')

    assert expected_result == actual_result


def test_get_snmpalert_id_with_correct_name(api, constants):
    expected_result = constants['snmpalert_id']
    actual_result = api.get_snmpalert_id(constants['snmpalert'])

    assert expected_result == actual_result


def test_get_snmpalert_id_with_incorrect_name(api, constants):
    expected_result = None
    actual_result = api.get_snmpalert_id('INCORRECT-NAME')

    assert expected_result == actual_result
