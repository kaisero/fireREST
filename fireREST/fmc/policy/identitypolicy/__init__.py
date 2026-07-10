from fireREST.defaults import API_RELEASE_700, API_RELEASE_1000
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.identitypolicy.identitycategory import IdentityCategory
from fireREST.fmc.policy.identitypolicy.identityrule import IdentityRule


class IdentityPolicy(Resource):
    """Retrieves the Identity Policy associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIdentityPolicy` (GET (list))
    - `getIdentityPolicy` (GET)
    - `createIdentityPolicy` (CREATE)
    - `updateIdentityPolicy` (UPDATE)
    - `deleteIdentityPolicy` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/identitypolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_1000

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.identitycategory = IdentityCategory(conn)
        self.identityrule = IdentityRule(conn)
