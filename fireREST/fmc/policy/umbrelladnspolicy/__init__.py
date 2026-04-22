from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.umbrelladnspolicy.umbrelladnsrule import UmbrellaDnsRule


class UmbrellaDnsPolicy(Resource):
    PATH = '/policy/umbrelladnspolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.umbrelladnsrule = UmbrellaDnsRule(conn)
