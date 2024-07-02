# -*- coding: utf-8 -*-

import pytest


from fireREST.fmc import Connection
from fireREST import exceptions as exc


@pytest.fixture
def connection(cdo_constants):
    return Connection(
        hostname=cdo_constants['hostname'],
        password=cdo_constants['password'],
        cdo=True
    )

def test_cdo_auth_wrong_credentials(cdo_constants):
    with pytest.raises(exc.AuthError):
        Connection(
            hostname=cdo_constants['hostname'],
            password="THIS-TOKEN-IS-EXPECTED-TO-BE-WRONG",
            cdo=True
        )

def test_cdo_get_version(connection):
    connection.login()
    print(connection.hostname)
    actual_result = connection.get_version()

    assert actual_result is not None
