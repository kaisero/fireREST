# -*- coding: utf-8 -*-

import pytest

from fireREST import Client
from fireREST.defaults import API_AUTH_URL, API_REFRESH_URL, API_PLATFORM_URL, API_CONFIG_URL


def test_sanitize_with_valid_dict_payload(api):
    method = 'PUT'
    payload = {
        'id': 'A-VALID-UUID',
        'name': 'TEST-OBJ',
        'metadata': {'domain': 'Global'},
        'links': {'self': 'https://fmc.example.com'},
    }
    expected_result = {'id': 'A-VALID-UUID', 'name': 'TEST-OBJ'}
    actual_result = api._sanitize(method, payload)
    assert actual_result == expected_result


def test_sanitize_with_valid_dict_payload_and_post_operation(api):
    method = 'post'
    payload = {
        'id': 'A-VALID-UUID',
        'name': 'TEST-OBJ',
        'metadata': {'domain': 'Global'},
        'links': {'self': 'https://fmc.example.com'},
    }
    expected_result = {'name': 'TEST-OBJ'}
    actual_result = api._sanitize(method, payload)
    assert actual_result == expected_result


def test_sanitize_with_valid_list_payload(api):
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
    actual_result = api._sanitize(method, payload)
    assert actual_result == expected_result


def test_sanitize_with_valid_list_payload_and_post_operation(api):
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
    actual_result = api._sanitize(method, payload)
    assert actual_result == expected_result


def test_virtualrouter_support_with_virtualrouter_param(api):
    virtualrouter_id = '1111-1111'
    expected_result = f'/devices/devicerecords/0000-0000/routing/virtualrouters/{virtualrouter_id}/ipv4staticroutes'
    actual_result = api._virtualrouter_url(
        '/devices/devicerecords/0000-0000/routing/ipv4staticroutes', virtualrouter_id
    )
    assert actual_result == expected_result


def test_virtualrouter_support_without_virtualrouter_param(api):
    expected_result = f'/devices/devicerecords/0000-0000/routing/ipv4staticroutes'
    actual_result = api._virtualrouter_url(expected_result)
    assert actual_result == expected_result


def test_filter_with_single_item(api):
    expected_filter = 'deviceId:457d932a-3dfb-11ea-9b36-8a42de410c5c'
    actual_filter = api._filter(items={'deviceId': '457d932a-3dfb-11ea-9b36-8a42de410c5c'})
    assert actual_filter == expected_filter


def test_filter_with_multiple_items(api):
    expected_filter = 'deviceId:457d932a-3dfb-11ea-9b36-8a42de410c5c;ids:00505699-76B7-0ed3-0000-000268437535'
    actual_filter = api._filter(
        items={'deviceId': '457d932a-3dfb-11ea-9b36-8a42de410c5c', 'ids': '00505699-76B7-0ed3-0000-000268437535'}
    )
    assert actual_filter == expected_filter


def test_filter_with_empty_input(api):
    expected_filter = ''
    actual_filter = api._filter(items={})
    assert actual_filter == expected_filter


def test_filter_with_invalid_input(api):
    expected_filter = ''
    actual_filter = api._filter(items={'valueempty': None})
    assert actual_filter == expected_filter


def test_default_url(api):
    expected_url = f'{api.protocol}://{api.hostname}/test'
    actual_url = api._url(path='/test')
    assert actual_url == expected_url


def test_config_url(api):
    expected_url = f'{api.protocol}://{api.hostname}{API_CONFIG_URL}/domain/{api.domain}/test'
    actual_url = api._url(namespace='config', path='/test')
    assert actual_url == expected_url


def test_platform_url(api):
    expected_url = f'{api.protocol}://{api.hostname}{API_PLATFORM_URL}/test'
    actual_url = api._url(namespace='platform', path='/test')
    assert actual_url == expected_url


def test_refresh_url(api):
    expected_url = f'{api.protocol}://{api.hostname}{API_REFRESH_URL}'
    actual_url = api._url(namespace='refresh', path='/test')
    assert actual_url == expected_url
