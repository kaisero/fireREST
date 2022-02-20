# -*- coding: utf-8 -*-

from fireREST.fmc.assignment import Assignment
from fireREST.fmc.audit import Audit
from fireREST.fmc.chassis import Chassis
from fireREST.fmc.device import Device
from fireREST.fmc.devicecluster import DeviceCluster
from fireREST.fmc.devicehapair import DeviceHAPair
from fireREST.fmc.devicegroup import DeviceGroup
from fireREST.fmc.deployment import Deployment
from fireREST.fmc.health import Health
from fireREST.fmc.integration import Integration
from fireREST.fmc.intelligence import Intelligence
from fireREST.fmc.job import Job
from fireREST.fmc.netmap import NetMap
from fireREST.fmc.object import Object
from fireREST.fmc.policy import Policy
from fireREST.fmc.system import System
from fireREST.fmc.update import Update
from fireREST.fmc.user import User


def test_initialization(fmc):
    assert isinstance(fmc.assignment, Assignment)
    assert isinstance(fmc.audit, Audit)
    assert isinstance(fmc.chassis, Chassis)
    assert isinstance(fmc.device, Device)
    assert isinstance(fmc.devicecluster, DeviceCluster)
    assert isinstance(fmc.devicehapair, DeviceHAPair)
    assert isinstance(fmc.devicegroup, DeviceGroup)
    assert isinstance(fmc.deployment, Deployment)
    assert isinstance(fmc.health, Health)
    assert isinstance(fmc.integration, Integration)
    assert isinstance(fmc.intelligence, Intelligence)
    assert isinstance(fmc.job, Job)
    assert isinstance(fmc.netmap, NetMap)
    assert isinstance(fmc.object, Object)
    assert isinstance(fmc.policy, Policy)
    assert isinstance(fmc.system, System)
    assert isinstance(fmc.update, Update)
    assert isinstance(fmc.user, User)
