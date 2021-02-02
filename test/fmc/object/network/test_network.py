# -*- coding: utf-8 -*-

from fireREST.fmc.object.network.override import Override
from test.conftest import STATE



def test_initialization(fmc):
    network = fmc.object.network
    assert isinstance(network.override, Override)


def test_create_network_object(fmc):
    expected_result = 201
    data = {'name': 'FireREST-NetworkObj', 'value': '198.18.1.0/24'}

    actual_result = fmc.object.network.create(data)
    STATE['object']['network'] = actual_result.json()
    actual_result = actual_result.status_code

    assert expected_result == actual_result


def test_get_network_objects(fmc):
    expected_result = 'FireREST-NetworkObj'
    actual_result = None

    for item in fmc.object.network.get():
        if item['name'] == expected_result:
            actual_result = item['name']

    assert expected_result == actual_result


def test_get_network_object_by_name(fmc):
    expected_result = 'FireREST-NetworkObj'
    actual_result = fmc.object.network.get(name=expected_result)['name']

    assert expected_result == actual_result


def test_get_network_object_by_id(fmc):
    expected_result = fmc.object.network.get(name=STATE['object']['network']['name'])['id']
    actual_result = fmc.object.network.get(uuid=expected_result)['id']

    assert expected_result == actual_result


def test_update_network_object(fmc):
    data = fmc.object.network.get(name=STATE['object']['network']['name'])
    data['description'] = 'Description set by FireREST'
    expected_result = 200
    actual_result = fmc.object.network.update(data).status_code

    assert expected_result == actual_result


def test_delete_network_object(fmc):
    expected_result = 200
    obj_id = fmc.object.network.get(name=STATE['object']['network']['name'])['id']
    actual_result = fmc.object.network.delete(uuid=obj_id).status_code

    assert expected_result == actual_result
