# -*- coding: utf-8 -*-

import pytest

from fireREST import Client
from fireREST.defaults import API_AUTH_URL, API_REFRESH_URL, API_PLATFORM_URL, API_CONFIG_URL


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
