from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.zerotrustpolicy.application import Application
from fireREST.fmc.policy.zerotrustpolicy.applicationgroup import ApplicationGroup


class ZeroTrustPolicy(Resource):
    """Retrieves the Zero Trust policy associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllZeroTrustPolicy` (GET (list))
    - `getZeroTrustPolicy` (GET)
    - `createZeroTrustPolicy` (CREATE)
    - `updateZeroTrustPolicy` (UPDATE)
    - `deleteZeroTrustPolicy` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To filter policies.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/zerotrustpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.application = Application(conn)
        self.applicationgroup = ApplicationGroup(conn)
