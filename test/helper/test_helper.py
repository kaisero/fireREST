# -*- coding: utf-8 -*-

import pytest

from fireREST import Client
from fireREST.defaults import API_AUTH_URL, API_REFRESH_URL, API_PLATFORM_URL, API_CONFIG_URL


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
