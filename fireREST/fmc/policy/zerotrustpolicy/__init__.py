from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.zerotrustpolicy.application import Application
from fireREST.fmc.policy.zerotrustpolicy.applicationgroup import ApplicationGroup


class ZeroTrustPolicy(Resource):
    PATH = '/policy/zerotrustpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.application = Application(conn)
        self.applicationgroup = ApplicationGroup(conn)
