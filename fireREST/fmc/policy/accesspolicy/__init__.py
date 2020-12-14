from typing import Dict

from fireREST.defaults import API_CONFIG_NAME
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.accesspolicy.accessrule import AccessRule


class AccessPolicy(Resource):
    PATH = '/policy/accesspolicies/{uuid}'
    SUPPORTED_OPERATIONS = ['create', 'get', 'update', 'delete']

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.accessrule = AccessRule(conn)
