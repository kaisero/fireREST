# -*- coding: utf-8 -*-

import pytest

from fireREST import FMC
from fireREST.fmc import Connection


STATE = {
    'object': {'network': {'name': 'FireREST-NetworkObj'}},
    'policy': {
        'accesspolicy': {
            'name': 'FireREST-AccessPolicy',
            'accessrule': {'name': 'FireREST-AccessRule'},
        },
        'ftdnatpolicy': {
            'name': 'FireREST-NatPolicy',
            'manualnatrule': {'name': 'FireREST-ManualNatRule'},
        },
    },
    'device': {'devicerecord': {'name': 'ftd-01'}},
}


@pytest.fixture(scope='module')
def constants():
    return {
        'hostname': '10.62.158.192',
        'username': 'api',
        'password': 'Cisco123!',
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
def cdo_constants():
    return {
        'hostname': 'cisco-rchrabas--sbs3cp.app.eu.cdo.cisco.com',
        'password': 'eyJraWQiOiIwIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOiIwIiwicm9sZXMiOlsiUk9MRV9TVVBFUl9BRE1JTiJdLCJhbXIiOiJzYW1sIiwiaXNzIjoiaXRkIiwiY2x1c3RlcklkIjoiMyIsInN1YmplY3RUeXBlIjoidXNlciIsImNsaWVudF9pZCI6ImFwaS1jbGllbnQiLCJwYXJlbnRJZCI6ImFjNzkzYjFjLWVlOGEtNDY4MS1iNmEwLTA0YTJjZGM4ZDJhMSIsInNjb3BlIjpbInRydXN0IiwicmVhZCIsImFjNzkzYjFjLWVlOGEtNDY4MS1iNmEwLTA0YTJjZGM4ZDJhMSIsIndyaXRlIl0sImlkIjoiMzYwN2U2YWEtYTA2ZS00ZTY1LTg4NGEtYzY3ZTY0MGFlNTU5IiwiZXhwIjozODk0ODAwNTc5LCJyZWdpb24iOiJwcm9kZXUiLCJpYXQiOjE3NDczMTY5OTIsImp0aSI6IjU5NDhlM2QxLTIyZWItNGRiMC05NWI2LWY2MTY4Y2NmZDA4OCJ9.w3HiccnnKGTPHXrX3yqWLy5PurOR7uxdZo5Fwjc_8avsS01KURr2WJqUGzBnGHjLff7Xmt_SVdp-vxYG279yTHGfT9GWZYVNWl1YAmKb2-xIan6gIxsIjvKa038YTvTjWkYQ-HgpoaKk8Z8w0d3vj7bf8Vu4ZivutRsIgqg_ClkeLzazX_GmqREJHFEl20twXGXbDb245N0dMjEcs743CdYiES1ep2pgQqBHZAIVPx3m4VllDM3a4k6Hz2JWYdaR9NN2Lt1fav64T2puTzffOztwdUCg9PHZGwQDa0NX1P2GScZg93_5FgNUPk8F2VzXhdDdArBSXm67S73_jHsxyg',
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


@pytest.fixture(scope='module')
def cdo_fmc(cdo_constants):
    return FMC(
        hostname=cdo_constants['hostname'],
        password=cdo_constants['password'],
        cdo=True,
    )


@pytest.fixture(scope='module')
def devicerecord(fmc):
    return fmc.device.devicerecord.get(name=STATE['device']['devicerecord']['name'])


@pytest.fixture(scope='module')
def virtualrouter(fmc, devicerecord):
    return fmc.device.devicerecord.routing.virtualrouter.get(container_uuid=devicerecord['id'])[0]
