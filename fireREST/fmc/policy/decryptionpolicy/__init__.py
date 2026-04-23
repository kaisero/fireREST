from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.decryptionpolicy.decryptionpolicyrule import DecryptionPolicyRule


class DecryptionPolicy(Resource):
    PATH = '/policy/decryptionpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.decryptionpolicyrule = DecryptionPolicyRule(conn)
