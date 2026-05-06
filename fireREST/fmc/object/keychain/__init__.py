from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.keychain.override import Override


class KeyChain(Resource):
    """Retrieves, deletes, creates, or modifies the Keychain object associated with the specified ID. If no ID is specified for a GET, retrieves list of all Keychain objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllKeyChainObject` (GET (list))
    - `getKeyChainObject` (GET)
    - `createMultipleKeyChainObject` (CREATE)
    - `updateKeyChainObject` (UPDATE)
    - `deleteKeyChainObject` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the KeyChain object on given target ID.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for KeyChain objects.
    """
    PATH = '/object/keychains/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_640

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
