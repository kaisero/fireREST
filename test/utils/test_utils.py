# -*- coding: utf-8 -*-

import pytest

from uuid import uuid4

from fireREST import utils


def test_is_uuid_with_valid_uuid():
    valid_uuid = str(uuid4())
    expected_result = True

    actual_result = utils.is_uuid(valid_uuid)

    assert expected_result == actual_result


def test_is_uuid_with_invalid_uuid():
    invalid_uuid = str('override')
    expected_result = False

    actual_result = utils.is_uuid(invalid_uuid)

    assert expected_result == actual_result


def test_is_getbyid_operation_with_valid_getbyid_operation():
    valid_getbyid_operation = 'https://localhost' \
                              '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f' \
                              '/object/networkgroups/A09351F4-691E-0ed3-0000-034359739130'
    expected_result = True

    actual_result = utils.is_getbyid_operation(valid_getbyid_operation)

    assert expected_result == actual_result


def test_is_getbyid_operation_with_valid_getbyid_operation_with_params():
    valid_getbyid_operation = 'https://localhost' \
                              '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f' \
                              '/object/networkgroups/A09351F4-691E-0ed3-0000-034359739130?expanded=True'
    expected_result = True

    actual_result = utils.is_getbyid_operation(valid_getbyid_operation)

    assert expected_result == actual_result


def test_is_getbyid_operation_with_invalid_getbyid_operation():
    valid_getbyid_operation = 'https://localhost' \
                              '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f' \
                              '/object/networkgroups/A09351F4-691E-0ed3-0000-034359739130/overrides'
    expected_result = False

    actual_result = utils.is_getbyid_operation(valid_getbyid_operation)

    assert expected_result == actual_result
