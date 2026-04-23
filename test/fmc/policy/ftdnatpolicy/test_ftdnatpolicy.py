# -*- coding: utf-8 -*-
from fireREST.fmc.policy.ftdnatpolicy.autonatrule import AutoNatRule
from fireREST.fmc.policy.ftdnatpolicy.manualnatrule import ManualNatRule
from fireREST.fmc.policy.ftdnatpolicy.natrule import NatRule

from test.conftest import STATE


def test_initialization(fmc):
    ftdnatpolicy = fmc.policy.ftdnatpolicy

    assert isinstance(ftdnatpolicy.autonatrule, AutoNatRule)
    assert isinstance(ftdnatpolicy.manualnatrule, ManualNatRule)
    assert isinstance(ftdnatpolicy.natrule, NatRule)


def test_create_ftdnatpolicy(fmc):
    expected_result = 201
    data = {'name': STATE['policy']['ftdnatpolicy']['name']}

    actual_result = fmc.policy.ftdnatpolicy.create(data).status_code

    assert expected_result == actual_result


def test_delete_ftdnatpolicy(fmc):
    expected_result = 200

    actual_result = fmc.policy.ftdnatpolicy.delete(name=STATE['policy']['ftdnatpolicy']['name']).status_code

    assert expected_result == actual_result
