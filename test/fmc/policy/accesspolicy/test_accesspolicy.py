# -*- coding: utf-8 -*-

from fireREST.fmc.policy.accesspolicy import AccessRule
from test.conftest import STATE

STATE['name'] = 'FireREST-AccessPolicy'


def test_initialization(fmc):
    actual_accessrule = fmc.policy.accesspolicy.accessrule
    assert isinstance(actual_accessrule, AccessRule)


def test_create_accesspolicy(fmc):
    expected_result = 201
    data = {'name': STATE['name'], 'defaultAction': {'action': 'BLOCK'}}

    actual_result = fmc.policy.accesspolicy.create(data).status_code

    assert expected_result == actual_result


def test_get_accesspolicies(fmc):
    expected_result = STATE['name']
    actual_result = None

    for item in fmc.policy.accesspolicy.get():
        if item['name'] == expected_result:
            actual_result = item['name']

    assert expected_result == actual_result


def test_get_accesspolicy_by_name(fmc):
    expected_result = STATE['name']
    actual_result = fmc.policy.accesspolicy.get(name=STATE['name'])['name']

    assert expected_result == actual_result


def test_get_accesspolicy_by_id(fmc):
    expected_result = STATE['name']
    accesspolicy_id = fmc.policy.accesspolicy.get(name=STATE['name'])['id']
    actual_result = fmc.policy.accesspolicy.get(uuid=accesspolicy_id)['name']

    assert expected_result == actual_result


def test_update_accesspolicy(fmc):
    data = fmc.policy.accesspolicy.get(name=STATE['name'])
    data['name'] = 'FireREST-AccessPolicyUpdated'
    STATE['name'] = data['name']
    expected_result = 200
    actual_result = fmc.policy.accesspolicy.update(data).status_code

    assert expected_result == actual_result


def test_delete_accesspolicy(fmc):
    expected_result = 200
    accesspolicy_id = fmc.policy.accesspolicy.get(name=STATE['name'])['id']
    actual_result = fmc.policy.accesspolicy.delete(uuid=accesspolicy_id).status_code

    assert expected_result == actual_result
