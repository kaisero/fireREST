# -*- coding: utf-8 -*-

from fireREST.fmc.policy.accesspolicy import AccessRule
from test.conftest import STATE


def test_initialization(fmc):
    actual_accessrule = fmc.policy.accesspolicy.accessrule
    assert isinstance(actual_accessrule, AccessRule)


def test_create_accesspolicy(fmc):
    accesspolicy = {'name': 'FireREST-AccessPolicy', 'defaultAction': {'action': 'BLOCK'}}

    expected_result = accesspolicy['name']
    STATE['accesspolicy'] = fmc.policy.accesspolicy.create(accesspolicy).json()
    actual_result = STATE['accesspolicy']['name']

    assert expected_result == actual_result


def test_get_accesspolicies(fmc):
    expected_result = STATE['accesspolicy']['id']
    actual_result = None

    for item in fmc.policy.accesspolicy.get():
        if item['id'] == expected_result:
            actual_result = item['id']

    assert expected_result == actual_result


def test_get_accesspolicy_by_name(fmc):
    expected_result = STATE['accesspolicy']['id']
    actual_result = fmc.policy.accesspolicy.get(name=STATE['accesspolicy']['name'])['id']

    assert expected_result == actual_result


def test_get_accesspolicy_by_id(fmc):
    expected_result = STATE['accesspolicy']['id']
    STATE['accesspolicy'] = fmc.policy.accesspolicy.get(uuid=STATE['accesspolicy']['id'])
    actual_result = STATE['accesspolicy']['id']

    assert expected_result == actual_result


def test_update_accesspolicy(fmc):

    STATE['accesspolicy']['name'] = 'RenamedAccessPolicy'
    expected_result = 200
    actual_result = fmc.policy.accesspolicy.update(STATE['accesspolicy']).status_code

    assert expected_result == actual_result


def test_delete_accesspolicy(fmc):
    expected_result = 200
    actual_result = fmc.policy.accesspolicy.delete(uuid=STATE['accesspolicy']['id']).status_code

    assert expected_result == actual_result
