# -*- coding: utf-8 -*-

import copy
import uuid
import packaging

import pytest

import fireREST.exceptions as exc

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


def test_create_accesspolicy_with_name_that_already_exists(fmc):
    with pytest.raises(exc.ResourceAlreadyExistsError):
        data = {'name': STATE['name'], 'defaultAction': {'action': 'BLOCK'}}
        fmc.policy.accesspolicy.create(data)


def test_create_accesspolicy_with_invalid_payload(fmc):
    with pytest.raises(exc.UnprocessableEntityError):
        data = {'invalid': 'payload'}
        fmc.policy.accesspolicy.create(data)


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


def test_get_accesspolicy_by_name_with_nonexisting_name(fmc):
    with pytest.raises(exc.ResourceNotFoundError):
        fmc.policy.accesspolicy.get(name='InvalidAccessPolicy')


def test_get_accesspolicy_by_id(fmc):
    expected_result = STATE['name']
    accesspolicy_id = fmc.policy.accesspolicy.get(name=STATE['name'])['id']
    actual_result = fmc.policy.accesspolicy.get(uuid=accesspolicy_id)['name']

    assert expected_result == actual_result


def test_get_accesspolicy_by_uuid_with_nonexisting_uuid(fmc):
    with pytest.raises(exc.ResourceNotFoundError):
        nonexisting_uuid = uuid.uuid1()
        fmc.policy.accesspolicy.get(uuid=nonexisting_uuid)


def test_get_accesspolicies_with_incompatible_fmc_release(fmc):
    accesspolicy = copy.deepcopy(fmc.policy.accesspolicy)
    accesspolicy.version = packaging.version.parse('6.0.0')
    with pytest.raises(exc.UnsupportedOperationError):
        accesspolicy.get()


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
