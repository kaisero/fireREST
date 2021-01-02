# -*- coding: utf-8 -*-

import logging

from . import defaults
from . import exceptions as exc
from . import utils
from .fmc import Connection, Resource
from .fmc.assignment import Assignment
from .fmc.audit import Audit
from .fmc.device import Device
from .fmc.devicecluster import DeviceCluster
from .fmc.devicehapair import DeviceHAPair
from .fmc.devicegroup import DeviceGroup
from .fmc.deployment import Deployment
from .fmc.health import Health
from .fmc.integration import Integration
from .fmc.intelligence import Intelligence
from .fmc.object import Object
from .fmc.policy import Policy
from .fmc.system import System
from .fmc.update import Update
from .fmc.user import User


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class FMC(Resource):

    def __init__(
        self,
        hostname: str,
        username: str,
        password: str,
        protocol=defaults.API_PROTOCOL,
        verify_cert=False,
        domain=defaults.API_DEFAULT_DOMAIN,
        timeout=defaults.API_REQUEST_TIMEOUT,
    ):
        self.conn = Connection(hostname, username, password, protocol, verify_cert, domain, timeout)
        self.domain = self.conn.domain
        self.version = self.conn.version
        self.assignment = Assignment(self.conn)
        self.audit = Audit(self.conn)
        self.deployment = Deployment(self.conn)
        self.device = Device(self.conn)
        self.devicecluster = DeviceCluster(self.conn)
        self.devicehapair = DeviceHAPair(self.conn)
        self.devicegroup = DeviceGroup(self.conn)
        self.health = Health(self.conn)
        self.integration = Integration(self.conn)
        self.intelligence = Intelligence(self.conn)
        self.object = Object(self.conn)
        self.policy = Policy(self.conn)
        self.system = System(self.conn)
        self.update = Update(self.conn)
        self.user = User(self.conn)
