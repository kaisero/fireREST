# -*- coding: utf-8 -*-

import logging

from . import defaults
from . import exceptions as exc
from . import utils
from .fmc import Connection, Resource
from .fmc.assignment import Assignment
from.fmc.audit import Audit
from .fmc.integration import Integration
from .fmc.object import Object
from .fmc.policy import Policy
from .fmc.system import System
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
        self.integration = Integration(self.conn)
        self.object = Object(self.conn)
        self.policy = Policy(self.conn)
        self.system = System(self.conn)
        self.user = User(self.conn)
