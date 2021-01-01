# -*- coding: utf-8 -*-
import copy
import packaging
import pytest
import uuid

from test.conftest import STATE
from fireREST import exceptions as exc
from fireREST.fmc.policy.accesspolicy.accessrule import AccessRule


@pytest.fixture(scope='module')
def accesspolicy(request, fmc):

    data = {'name': STATE['policy']['accesspolicy']['name'], 'defaultAction': {'action': 'BLOCK'}}
    policy = fmc.policy.accesspolicy.create(data).json()

    def teardown():
        fmc.policy.accesspolicy.delete(uuid=policy['id'])
    request.addfinalizer(teardown)

    return policy


def test_initialization(fmc, accesspolicy):
    actual_accessrule = fmc.policy.accesspolicy.accessrule
    assert isinstance(actual_accessrule, AccessRule)


def test_create_accessrule(fmc, accesspolicy):
    expected_result = 201
    data = {'name': STATE['policy']['accesspolicy']['accessrule']['name'], 'action': 'ALLOW'}

    response = fmc.policy.accesspolicy.accessrule.create(container_uuid=accesspolicy['id'], data=data)
    STATE['policy']['accesspolicy']['accessrule'] = response.json()
    actual_result = response.status_code

    assert expected_result == actual_result


def test_create_accessrules_using_bulk_operation(fmc, accesspolicy):
    expected_result = 201
    data = [
        {'name': 'BulkRule01', 'action': 'ALLOW'},
        {'name': 'BulkRule02', 'action': 'ALLOW'}
    ]

    response = fmc.policy.accesspolicy.accessrule.create(container_uuid=accesspolicy['id'], data=data)
    actual_result = response.status_code

    assert expected_result == actual_result


def test_create_accessrule_in_mandatory_section(fmc, accesspolicy):
    expected_result = 201
    data = {'name': 'MandatoryAccessRule', 'action': 'ALLOW'}

    actual_result = fmc.policy.accesspolicy.accessrule.create(container_uuid=accesspolicy['id'],
                                                              section='Mandatory',
                                                              data=data).status_code

    assert expected_result == actual_result


def test_create_accessrule_in_default_section(fmc, accesspolicy):
    expected_result = 201
    data = {'name': 'DefaultAccessRule', 'action': 'ALLOW'}

    actual_result = fmc.policy.accesspolicy.accessrule.create(container_uuid=accesspolicy['id'],
                                                              section='Default',
                                                              data=data).status_code

    assert expected_result == actual_result


def test_create_accessrule_with_invalid_section_should_fail_with_generic_api_error(fmc, accesspolicy):
    with pytest.raises(exc.GenericApiError) as excinfo:
        def f():
            data = {'name': 'DefaultAccessRule', 'action': 'ALLOW'}
            actual_result = fmc.policy.accesspolicy.accessrule.create(container_uuid=accesspolicy['id'],
                                                                      section='InvalidSection',
                                                                      data=data)
        f()

    assert str(excinfo.value) == 'Only mandatory and default are the allowed option in parameter section'


def test_get_accessrules(fmc, accesspolicy):
    expected_result = STATE['policy']['accesspolicy']['accessrule']['name']
    actual_result = None

    for item in fmc.policy.accesspolicy.accessrule.get(container_uuid=accesspolicy['id']):
        if item['name'] == expected_result:
            actual_result = item['name']

    assert expected_result == actual_result


def get_accessrules_by_accesspolicy_name(fmc, accesspolicy):
    expected_result = STATE['policy']['accesspolicy']['accessrule']['name']
    actual_result = None

    for item in fmc.policy.accesspolicy.accessrule.get(container_name=accesspolicy['name']):
        if item['name'] == expected_result:
            actual_result = item['name']

    assert expected_result == actual_result


def test_get_accessrule_by_name(fmc, accesspolicy):
    accessrule = STATE['policy']['accesspolicy']['accessrule']
    expected_result = STATE['policy']['accesspolicy']['accessrule']['name']
    actual_result = fmc.policy.accesspolicy.accessrule.get(container_uuid=accesspolicy['id'],
                                                           name=accessrule['name'])['name']

    assert expected_result == actual_result


def test_get_accessrule_by_name_with_nonexisting_name(fmc, accesspolicy):
    with pytest.raises(exc.ResourceNotFoundError):
        fmc.policy.accesspolicy.accessrule.get(container_uuid=accesspolicy['id'], name='InvalidAccessPolicy')


def test_get_accessrule_by_uuid(fmc, accesspolicy):
    expected_result = STATE['policy']['accesspolicy']['accessrule']['name']
    accessrule_id = fmc.policy.accesspolicy.accessrule.get(container_uuid=accesspolicy['id'],
                                                           name=STATE['policy']['accesspolicy']['accessrule']['name'])['id']
    actual_result = fmc.policy.accesspolicy.accessrule.get(container_uuid=accesspolicy['id'],
                                                           uuid=accessrule_id)['name']

    assert expected_result == actual_result


def test_get_accessrule_by_uuid_with_nonexisting_uuid(fmc, accesspolicy):
    with pytest.raises(exc.ResourceNotFoundError):
        nonexisting_uuid = uuid.uuid1()
        fmc.policy.accesspolicy.accessrule.get(container_uuid=accesspolicy['id'], uuid=nonexisting_uuid)


def test_get_accesspolicies_with_incompatible_fmc_release(fmc, accesspolicy):
    accessrule = copy.deepcopy(fmc.policy.accesspolicy.accessrule)
    accessrule.version = packaging.version.parse('6.0.0')

    with pytest.raises(exc.UnsupportedOperationError):
        accessrule.get(container_uuid=accesspolicy['id'])


def test_update_accessrule(fmc, accesspolicy):
    STATE['policy']['accesspolicy']['accessrule']['name'] = 'FireREST-AccessRuleUpdated'
    data = STATE['policy']['accesspolicy']['accessrule']
    expected_result = 200
    actual_result = fmc.policy.accesspolicy.accessrule.update(container_uuid=accesspolicy['id'], data=data).status_code

    assert expected_result == actual_result


def test_delete_accessrule(fmc, accesspolicy):
    expected_result = 200
    actual_result = fmc.policy.accesspolicy.accessrule.delete(
        container_uuid=accesspolicy['id'],
        uuid=STATE['policy']['accesspolicy']['accessrule']['id']).status_code

    assert expected_result == actual_result


def test_delete_accessrule_with_invalid_container_uuid(fmc):
    with pytest.raises(exc.ResourceNotFoundError):
        fmc.policy.accesspolicy.accessrule.delete(uuid=uuid.uuid4())


def test_delete_accessrule_with_invalid_uuid(fmc, accesspolicy):
    with pytest.raises(exc.ResourceNotFoundError):
        fmc.policy.accesspolicy.accessrule.delete(container_uuid=accesspolicy['id'], uuid=uuid.uuid4())