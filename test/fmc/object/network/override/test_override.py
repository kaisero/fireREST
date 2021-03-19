# -*- coding: utf-8 -*-

import pytest

from test.conftest import STATE


@pytest.fixture(scope='module', autouse=True)
def setup(fmc):
    try:
        device = fmc.device.devicerecord.get(name=STATE['device']['devicerecord']['name'])
        net_obj = {
            'name': 'FireREST-NetworkObj',
            'value': '198.18.1.0/24',
            'overridable': True,
        }
        STATE['object']['network'] = fmc.object.network.create(data=net_obj).json()

        net_override = {
            'overrides': {
                'target': {'type': 'Device', 'id': device['id']},
                'parent': {'id': STATE['object']['network']['id']},
            },
            'value': '198.18.100.0/24',
            'name': STATE['object']['network']['name'],
            'id': STATE['object']['network']['id'],
        }
        STATE['object']['network']['override'] = fmc.object.network.update(data=net_override).json()

        yield
    finally:
        if 'id' not in STATE['object']['network']:
            STATE['object']['network']['id'] = fmc.object.network.get(name=STATE['object']['network']['name'])['id']
        fmc.object.network.delete(uuid=STATE['object']['network']['id'])


def test_get_network_object_overrides(fmc):
    expected_result = STATE['object']['network']['override']['overrides']['target']['id']
    actual_result = None

    for item in fmc.object.network.override.get(container_uuid=STATE['object']['network']['id']):
        if item['overrides']['target']['id'] == expected_result:
            actual_result = item['overrides']['target']['id']

    assert expected_result == actual_result
