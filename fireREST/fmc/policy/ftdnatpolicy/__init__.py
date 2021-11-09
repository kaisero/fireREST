from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.ftdnatpolicy.autonatrule import AutoNatRule
from fireREST.fmc.policy.ftdnatpolicy.manualnatrule import ManualNatRule
from fireREST.fmc.policy.ftdnatpolicy.natrule import NatRule


class FtdNatPolicy(Resource):
    PATH = '/policy/ftdnatpolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_623

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.autonatrule = AutoNatRule(conn)
        self.manualnatrule = ManualNatRule(conn)
        self.natrule = NatRule(conn)
