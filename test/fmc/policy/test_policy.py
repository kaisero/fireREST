# -*- coding: utf-8 -*-

from fireREST.fmc.policy.accesspolicy import AccessPolicy


def test_initialization(fmc):
    actual_accesspolicy = fmc.policy.accesspolicy
    assert isinstance(actual_accesspolicy, AccessPolicy)
