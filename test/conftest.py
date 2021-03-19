# -*- coding: utf-8 -*-

import pytest

from fireREST import FMC
from fireREST.fmc import Connection


STATE = {
    'object': {'network': {'name': 'FireREST-NetworkObj'}},
    'policy': {
        'accesspolicy': {'name': 'FireREST-AccessPolicy', 'accessrule': {'name': 'FireREST-AccessRule'}},
        'ftdnatpolicy': {'name': 'FireREST-NatPolicy', 'manualnatrule': {'name': 'FireREST-ManualNatRule'}},
    },
    'device': {'devicerecord': {'name': 'ftd01.example.com'}},
}


@pytest.fixture(scope='module')
def constants():
    return {
        'hostname': 'fmc.example.com',
        'username': 'firerest',
        'password': 'ChangeMeForSecurity123!',
        'domain': {'name': 'Global/DEV'},
        'devicehapair': 'ftd01.example.com',
        'devicehapair_id': '6dd24c5c-0971-11eb-bde5-8c24580c007a',
        'device': 'ftd01.example.com',
        'device_id': '0ff8161e-096e-11eb-8ec0-cb721f246e60',
        'prefilterpolicy': 'PREFILTER-POLICY',
        'prefilterpolicy_id': '00505699-76B7-0ed3-0000-034359745152',
        'accesspolicy': 'ACCESS-POLICY',
        'accesspolicy_id': '00505699-76B7-0ed3-0000-034359744995',
        'accessrule': 'ACCESSRULE',
        'accessrule_id': '00505699-76B7-0ed3-0000-000268448801',
        'natpolicy': 'NAT-POLICY',
        'natpolicy_id': '00505699-76B7-0ed3-0000-034359745131',
        'syslogalert': 'SYSLOG-ALERT',
        'syslogalert_id': '6c0af500-0966-11eb-bde5-8c24580c007a',
        'snmpalert': 'SNMP-ALERT',
        'snmpalert_id': '65ad6f9e-0966-11eb-8883-d597dc3a0aca',
    }


@pytest.fixture(scope='module')
def conn(constants):
    return Connection(
        hostname=constants['hostname'],
        username=constants['username'],
        password=constants['password'],
        domain=constants['domain']['name'],
    )


@pytest.fixture(scope='module')
def fmc(constants):
    return FMC(
        hostname=constants['hostname'],
        username=constants['username'],
        password=constants['password'],
        domain=constants['domain']['name'],
    )
