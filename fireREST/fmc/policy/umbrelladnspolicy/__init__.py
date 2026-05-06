from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.umbrelladnspolicy.umbrelladnsrule import UmbrellaDnsRule


class UmbrellaDnsPolicy(Resource):
    """Retrieves the umbrella DNS policy associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllUmbrellaDNSPolicy` (GET (list))
    - `getUmbrellaDNSPolicy` (GET)
    - `createUmbrellaDNSPolicy` (CREATE)
    - `updateUmbrellaDNSPolicy` (UPDATE)
    - `deleteUmbrellaDNSPolicy` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/umbrelladnspolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.umbrelladnsrule = UmbrellaDnsRule(conn)
