# -*- coding: utf-8 -*-

import pytest


def test_get_deployabledevices_without_id_or_name(api, constants):
    deployabledevices = api.get_deployabledevices()
    expected_result = constants['device']
    actual_result = 'DeviceNotFoundInDeployAbleDevices'
    for item in deployabledevices:
        if item['name'] == expected_result:
            actual_result = item['name']

    assert expected_result == actual_result


def test_get_deployabledevices_with_name(api, constants):
    expected_result = constants['device']
    actual_result = api.get_deployabledevices(device_name=constants['device'])[0]['name']

    assert expected_result == actual_result
