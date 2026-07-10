from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.universalzerotrustrule import UniversalZeroTrustRule


class UniversalZeroTrustPolicy(Resource):
    """Retrieves or updates universal zero-trust policies.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllUniversalZeroTrustPolicy` (GET (list))
    - `getUniversalZeroTrustPolicy` (GET)
    - `updateUniversalZeroTrustPolicy` (UPDATE)
    """

    PATH = '/policy/universalzerotrustpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.universalzerotrustrule = UniversalZeroTrustRule(conn)
