from fireREST import utils
from fireREST.defaults import API_CONFIG_NAME
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.accesspolicy.accessrule import AccessRule
from fireREST.fmc.policy.accesspolicy.category import Category
from fireREST.fmc.policy.accesspolicy.defaultaction import DefaultAction
from fireREST.fmc.policy.accesspolicy.inheritancesettings import InheritanceSettings
from fireREST.fmc.policy.accesspolicy.operational import Operational


class AccessPolicy(Resource):
    PATH = '/policy/accesspolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.1.0'

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.accessrule = AccessRule(conn)
        self.category = Category(conn)
        self.defaultaction = DefaultAction(conn)
        self.inheritancesettings = InheritanceSettings(conn)
        self.operational = Operational(conn)
