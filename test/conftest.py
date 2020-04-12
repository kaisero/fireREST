# -*- coding: utf-8 -*-

import pytest

from fireREST import Client


@pytest.fixture(scope='module')
def constants():
    return {
        'hostname': 'fmc.example.com',
        'username': 'firerest',
        'password': 'Cisco123',
    }


@pytest.fixture(scope='module')
def api(constants):
    return Client(hostname=constants['hostname'], username=constants['username'], password=constants['password'])
