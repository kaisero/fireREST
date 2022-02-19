# -*- coding: utf-8 -*-

from fireREST.fmc.device.devicerecord.bridgegroupinterface import BridgeGroupInterface
from fireREST.fmc.device.devicerecord.etherchannelinterface import EtherChannelInterface
from fireREST.fmc.device.devicerecord.fpinterfacestatistics import FpInterfaceStatistics
from fireREST.fmc.device.devicerecord.fplogicalinterface import FpLogicalInterface
from fireREST.fmc.device.devicerecord.fpphysicalinterface import FpPhysicalInterface
from fireREST.fmc.device.devicerecord.inlineset import InlineSet
from fireREST.fmc.device.devicerecord.interfaceevent import InterfaceEvent
from fireREST.fmc.device.devicerecord.operational import Operational
from fireREST.fmc.device.devicerecord.physicalinterface import PhysicalInterface
from fireREST.fmc.device.devicerecord.redundantinterface import RedundantInterface
from fireREST.fmc.device.devicerecord.routing import Routing
from fireREST.fmc.device.devicerecord.subinterface import SubInterface
from fireREST.fmc.device.devicerecord.virtualswitch import VirtualSwitch
from fireREST.fmc.device.devicerecord.virtualtunnelinterface import VirtualTunnelInterface
from fireREST.fmc.device.devicerecord.vlaninterface import VlanInterface


def test_initialization(fmc):
    devicerecord = fmc.device.devicerecord
    assert isinstance(devicerecord.bridgegroupinterface, BridgeGroupInterface)
    assert isinstance(devicerecord.etherchannelinterface, EtherChannelInterface)
    assert isinstance(devicerecord.fpinterfacestatistics, FpInterfaceStatistics)
    assert isinstance(devicerecord.fplogicalinterface, FpLogicalInterface)
    assert isinstance(devicerecord.fpphysicalinterface, FpPhysicalInterface)
    assert isinstance(devicerecord.inlineset, InlineSet)
    assert isinstance(devicerecord.interfaceevent, InterfaceEvent)
    assert isinstance(devicerecord.operational, Operational)
    assert isinstance(devicerecord.physicalinterface, PhysicalInterface)
    assert isinstance(devicerecord.redundantinterface, RedundantInterface)
    assert isinstance(devicerecord.routing, Routing)
    assert isinstance(devicerecord.subinterface, SubInterface)
    assert isinstance(devicerecord.virtualswitch, VirtualSwitch)
    assert isinstance(devicerecord.virtualtunnelinterface, VirtualTunnelInterface)
    assert isinstance(devicerecord.vlaninterface, VlanInterface)
