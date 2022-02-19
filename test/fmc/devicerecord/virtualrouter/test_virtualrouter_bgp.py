# -*- coding: utf-8 -*-

from fireREST.fmc.device.devicerecord.routing.virtualrouter.bgp import Bgp


def test_initialization(fmc):
    bgp = fmc.device.devicerecord.routing.virtualrouter.bgp
    assert isinstance(bgp, Bgp)


def test_get_bgp_empty_configuration(fmc, devicerecord, virtualrouter):
    expected_result = []

    actual_result = fmc.device.devicerecord.routing.virtualrouter.bgp.get(container_uuid=devicerecord['id'],
                                                                          child_container_uuid=virtualrouter['id'])
    assert expected_result == actual_result
