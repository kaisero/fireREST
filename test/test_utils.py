# -*- coding: utf-8 -*-

import pytest

from uuid import uuid4

from fireREST import exceptions, utils


def test_is_uuid_with_valid_uuid():
    valid_uuid = str(uuid4())
    expected_result = True

    actual_result = utils.is_uuid(valid_uuid)

    assert expected_result == actual_result


def test_is_uuid_with_invalid_uuid():
    invalid_uuid = str('invalid-uuid')
    expected_result = False

    actual_result = utils.is_uuid(invalid_uuid)

    assert expected_result == actual_result


def test_is_getbyid_operation_with_valid_getbyid_operation():
    valid_getbyid_operation = (
        'https://localhost'
        '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f'
        '/object/networkgroups/A09351F4-691E-0ed3-0000-034359739130'
    )
    expected_result = True

    actual_result = utils.is_getbyid_operation(valid_getbyid_operation)

    assert expected_result == actual_result


def test_is_getbyid_operation_with_valid_getbyid_operation_with_params():
    valid_getbyid_operation = (
        'https://localhost'
        '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f'
        '/object/networkgroups/A09351F4-691E-0ed3-0000-034359739130?expanded=True'
    )
    expected_result = True

    actual_result = utils.is_getbyid_operation(valid_getbyid_operation)

    assert expected_result == actual_result


def test_is_getbyid_operation_with_invalid_getbyid_operation():
    valid_getbyid_operation = (
        'https://localhost'
        '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f'
        '/object/networkgroups/A09351F4-691E-0ed3-0000-034359739130/overrides'
    )
    expected_result = False

    actual_result = utils.is_getbyid_operation(valid_getbyid_operation)

    assert expected_result == actual_result


def test_validate_data_with_supported_payload_size():
    class ValidObject(object):
        def __init__(self):
            pass

        def __sizeof__(self):
            return 1024

    expected_result = None
    actual_result = utils.validate_data('post', ValidObject())

    assert expected_result == actual_result


def test_validate_data_with_unsupported_payload_size():
    with pytest.raises(exceptions.PayloadLimitExceededError):

        class InvalidObject(object):
            def __init__(self):
                pass

            def __sizeof__(self):
                return 204800100

        utils.validate_data('post', InvalidObject())


def test_sanitize_with_valid_dict_payload():
    method = 'PUT'
    payload = {
        'id': 'A-VALID-UUID',
        'name': 'TEST-OBJ',
        'metadata': {'domain': 'Global'},
        'links': {'self': 'https://fmc.example.com'},
    }
    expected_result = {'id': 'A-VALID-UUID', 'name': 'TEST-OBJ'}
    actual_result = utils.sanitize_payload(method, payload)
    assert actual_result == expected_result


def test_sanitize_with_valid_list_payload():
    method = 'PUT'
    payload = [
        {
            'id': 'A-VALID-UUID',
            'name': 'TEST-OBJ',
            'metadata': {'domain': 'Global'},
            'links': {'self': 'https://fmc.example.com'},
        }
    ]
    expected_result = [{'id': 'A-VALID-UUID', 'name': 'TEST-OBJ'}]
    actual_result = utils.sanitize_payload(method, payload)
    assert actual_result == expected_result


def test_sanitize_with_valid_list_payload_and_post_operation():
    method = 'post'
    payload = [
        {
            'id': 'A-VALID-UUID',
            'name': 'TEST-OBJ',
            'metadata': {'domain': 'Global'},
            'links': {'self': 'https://fmc.example.com'},
        }
    ]
    expected_result = [{'name': 'TEST-OBJ'}]
    actual_result = utils.sanitize_payload(method, payload)
    assert actual_result == expected_result


def test_search_filter_with_single_item():
    expected_filter = 'deviceId:457d932a-3dfb-11ea-9b36-8a42de410c5c'
    actual_filter = utils.search_filter(items=[{'deviceId': '457d932a-3dfb-11ea-9b36-8a42de410c5c'}])
    assert actual_filter == expected_filter


def test_search_filter_with_multiple_items():
    expected_filter = 'deviceId:457d932a-3dfb-11ea-9b36-8a42de410c5c;ids:00505699-76B7-0ed3-0000-000268437535'
    actual_filter = utils.search_filter(
        items=[{'deviceId': '457d932a-3dfb-11ea-9b36-8a42de410c5c'}, {'ids': '00505699-76B7-0ed3-0000-000268437535'}]
    )
    assert actual_filter == expected_filter


def test_search_filter_with_empty_input():
    expected_filter = ''
    actual_filter = utils.search_filter(items=[])
    assert actual_filter == expected_filter


def test_search_filter_with_invalid_input():
    expected_filter = ''
    actual_filter = utils.search_filter(items=[{'EmptyValue': None}])
    assert actual_filter == expected_filter
