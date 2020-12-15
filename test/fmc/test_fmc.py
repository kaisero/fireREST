# -*- coding: utf-8 -*-

from fireREST.fmc.object import Object
from fireREST.fmc.policy import Policy


def test_initialization(fmc):

    expected_object = Object
    expected_policy = Policy

    actual_object = fmc.object
    actual_policy = fmc.policy

    assert isinstance(actual_object, expected_object)
    assert isinstance(actual_policy, expected_policy)
