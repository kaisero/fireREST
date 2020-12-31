# -*- coding: utf-8 -*-
import pytest

from test.conftest import STATE
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

    actual_result = fmc.policy.accesspolicy.accessrule.create(container_uuid=accesspolicy['id'], data=data).status_code

    assert expected_result == actual_result

