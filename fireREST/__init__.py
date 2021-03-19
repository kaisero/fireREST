# -*- coding: utf-8 -*-

import logging

from fireREST import defaults
from fireREST import exceptions as exc
from fireREST import utils
from fireREST.fmc import Connection, Resource
from fireREST.fmc.assignment import Assignment
from fireREST.fmc.audit import Audit
from fireREST.fmc.deployment import Deployment
from fireREST.fmc.device import Device
from fireREST.fmc.devicecluster import DeviceCluster
from fireREST.fmc.devicehapair import DeviceHAPair
from fireREST.fmc.devicegroup import DeviceGroup
from fireREST.fmc.health import Health
from fireREST.fmc.integration import Integration
from fireREST.fmc.intelligence import Intelligence
from fireREST.fmc.job import Job
from fireREST.fmc.object import Object
from fireREST.fmc.policy import Policy
from fireREST.fmc.system import System
from fireREST.fmc.update import Update
from fireREST.fmc.user import User


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class FMC:
    def __init__(
        self,
        hostname: str,
        username: str,
        password: str,
        protocol=defaults.API_PROTOCOL,
        verify_cert=False,
        domain=defaults.API_DEFAULT_DOMAIN,
        timeout=defaults.API_REQUEST_TIMEOUT,
        dry_run=defaults.DRY_RUN,
    ):
        self.conn = Connection(hostname, username, password, protocol, verify_cert, domain, timeout, dry_run)
        self.domain = self.conn.domain
        self.version = self.conn.version
        self.assignment = Assignment(self.conn)
        self.audit = Audit(self.conn)
        self.deployment = Deployment(self.conn)
        self.device = Device(self.conn)
        self.devicecluster = DeviceCluster(self.conn)
        self.devicegroup = DeviceGroup(self.conn)
        self.devicehapair = DeviceHAPair(self.conn)
        self.health = Health(self.conn)
        self.integration = Integration(self.conn)
        self.intelligence = Intelligence(self.conn)
        self.job = Job(self.conn)
        self.object = Object(self.conn)
        self.policy = Policy(self.conn)
        self.system = System(self.conn)
        self.update = Update(self.conn)
        self.user = User(self.conn)
