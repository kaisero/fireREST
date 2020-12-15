# -*- coding: utf-8 -*-

import json
import logging
import re
import requests
import urllib3

from . import defaults
from . import exceptions as exc
from . import utils
from .fmc import Connection, Resource
from .fmc.object import Object
from .fmc.policy import Policy

from copy import deepcopy
from http.client import responses as http_responses
from packaging import version
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError
from time import sleep
from typing import Dict, List, Union
from urllib.parse import urlencode
from uuid import UUID

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class FMC(Resource):

    NAMESPACE = 'platform'
    PATH = '/'

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
        self.object = Object(self.conn)
        self.policy = Policy(self.conn)
