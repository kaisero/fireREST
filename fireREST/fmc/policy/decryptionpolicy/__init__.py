from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.decryptionpolicy.decryptionpolicyrule import DecryptionPolicyRule


class DecryptionPolicy(Resource):
    """Retrieves the decryption policy associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDecryptionPolicy` (GET (list))
    - `getDecryptionPolicy` (GET)
    - `createDecryptionPolicy` (CREATE)
    - `updateDecryptionPolicy` (UPDATE)
    - `deleteDecryptionPolicy` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter by name of the decryption policy is supported.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/decryptionpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.decryptionpolicyrule = DecryptionPolicyRule(conn)
