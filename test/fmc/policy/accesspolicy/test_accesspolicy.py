# -*- coding: utf-8 -*-

import copy
import uuid

import packaging
import pytest

import fireREST.exceptions as exc
from fireREST.fmc.policy.accesspolicy.accessrule import AccessRule
from fireREST.fmc.policy.accesspolicy.category import Category
from fireREST.fmc.policy.accesspolicy.defaultaction import DefaultAction
from fireREST.fmc.policy.accesspolicy.inheritancesettings import InheritanceSettings
from fireREST.fmc.policy.accesspolicy.operational import Operational
from test.conftest import STATE

name = STATE['policy']['accesspolicy']['name']


def test_initialization(fmc):
    accesspolicy = fmc.policy.accesspolicy
    assert isinstance(accesspolicy.accessrule, AccessRule)
    assert isinstance(accesspolicy.category, Category)
    assert isinstance(accesspolicy.defaultaction, DefaultAction)
    assert isinstance(accesspolicy.inheritancesettings, InheritanceSettings)
    assert isinstance(accesspolicy.operational, Operational)


def test_create_accesspolicy(fmc):
    expected_result = 201
    data = {'name': name, 'defaultAction': {'action': 'BLOCK'}}

    actual_result = fmc.policy.accesspolicy.create(data).status_code

    assert expected_result == actual_result


def test_create_accesspolicy_with_name_that_already_exists(fmc):
    with pytest.raises(exc.ResourceAlreadyExistsError):
        data = {'name': name, 'defaultAction': {'action': 'BLOCK'}}
        fmc.policy.accesspolicy.create(data)


def test_create_accesspolicy_with_invalid_payload(fmc):
    with pytest.raises(exc.UnprocessableEntityError):
        data = {'invalid': 'payload'}
        fmc.policy.accesspolicy.create(data)


def test_get_accesspolicies(fmc):
    expected_result = name
    actual_result = None

    for item in fmc.policy.accesspolicy.get():
        if item['name'] == expected_result:
            actual_result = item['name']

    assert expected_result == actual_result


def test_get_accesspolicy_by_name(fmc):
    expected_result = name
    actual_result = fmc.policy.accesspolicy.get(name=name)['name']

    assert expected_result == actual_result


def test_get_accesspolicy_by_name_with_nonexisting_name(fmc):
    with pytest.raises(exc.ResourceNotFoundError):
        fmc.policy.accesspolicy.get(name='InvalidAccessPolicy')


def test_get_accesspolicy_by_id(fmc):
    expected_result = name
    accesspolicy_id = fmc.policy.accesspolicy.get(name=name)['id']
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
    global name
    data = fmc.policy.accesspolicy.get(name=name)
    data['name'] = 'FireREST-AccessPolicyUpdated'
    name = data['name']
    expected_result = 200
    actual_result = fmc.policy.accesspolicy.update(data).status_code

    assert expected_result == actual_result


def test_update_accesspolicy_with_duplicate_resource(fmc):
    data = fmc.policy.accesspolicy.get(name=name)
    data['id'] = 'AccessPolicyThatDoesNotExist'

    with pytest.raises(exc.ResourceAlreadyExistsError):
        fmc.policy.accesspolicy.update(data)


def test_delete_accesspolicy(fmc):
    expected_result = 200
    accesspolicy_id = fmc.policy.accesspolicy.get(name=name)['id']
    actual_result = fmc.policy.accesspolicy.delete(uuid=accesspolicy_id).status_code

    assert expected_result == actual_result


def test_delete_accesspolicy_with_invalid_uuid(fmc):
    with pytest.raises(exc.ResourceNotFoundError):
        fmc.policy.accesspolicy.delete(uuid=uuid.uuid4())


def test_delete_accesspolicy_by_name(fmc):
    expected_result = 200
    policy_name = 'FireREST-AccessPolicyDeleteByName'
    data = {'name': policy_name, 'defaultAction': {'action': 'BLOCK'}}
    fmc.policy.accesspolicy.create(data)

    actual_result = fmc.policy.accesspolicy.delete(name=policy_name).status_code

    assert expected_result == actual_result
