# -*- coding: utf-8 -*-

from fireREST.fmc.object.network.override import Override
from test.conftest import STATE


def test_cdo_initialization(cdo_fmc):
    network = cdo_fmc.object.network
    assert isinstance(network.override, Override)


def test_cdo_create_network_object(cdo_fmc):
    expected_result = 201
    data = {'name': 'FireREST-NetworkObj', 'value': '198.18.1.0/24'}

    actual_result = cdo_fmc.object.network.create(data)
    STATE['object']['network'] = actual_result.json()
    actual_result = actual_result.status_code

    assert expected_result == actual_result


def test_cdo_create_network_object_bulk(cdo_fmc):
    expected_result = 201
    data = [
        {'name': 'FireREST-NetworkObjBulk1', 'value': '198.18.1.0/24'},
        {'name': 'FireREST-NetworkObjBulk2', 'value': '198.18.2.0/24'},
    ]

    actual_result = cdo_fmc.object.network.create(data)
    STATE['object']['network']['bulk'] = actual_result.json()
    actual_result = actual_result.status_code

    assert expected_result == actual_result


def test_cdo_get_network_objects(cdo_fmc):
    expected_result = 'FireREST-NetworkObj'
    actual_result = None

    for item in cdo_fmc.object.network.get():
        if item['name'] == expected_result:
            actual_result = item['name']

    assert expected_result == actual_result


def test_cdo_get_network_object_by_name(cdo_fmc):
    expected_result = 'FireREST-NetworkObj'
    actual_result = cdo_fmc.object.network.get(name=expected_result)['name']

    assert expected_result == actual_result


def test_cdo_get_network_object_by_id(cdo_fmc):
    expected_result = cdo_fmc.object.network.get(name=STATE['object']['network']['name'])['id']
    actual_result = cdo_fmc.object.network.get(uuid=expected_result)['id']

    assert expected_result == actual_result


def test_cdo_update_network_object(cdo_fmc):
    data = cdo_fmc.object.network.get(name=STATE['object']['network']['name'])
    data['description'] = 'Description set by FireREST'
    expected_result = 200
    actual_result = cdo_fmc.object.network.update(data).status_code

    assert expected_result == actual_result


def test_cdo_delete_network_object(cdo_fmc):
    expected_result = 200
    obj_id = cdo_fmc.object.network.get(name=STATE['object']['network']['name'])['id']
    actual_result = cdo_fmc.object.network.delete(uuid=obj_id).status_code

    assert expected_result == actual_result


def test_cdo_delete_network_object_bulk(cdo_fmc):
    expected_result = 200
    actual_result_first = cdo_fmc.object.network.delete(name='FireREST-NetworkObjBulk1').status_code
    actual_result_second = cdo_fmc.object.network.delete(name='FireREST-NetworkObjBulk2').status_code

    assert expected_result == actual_result_first
    assert expected_result == actual_result_second
