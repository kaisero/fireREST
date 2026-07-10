from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class LocalRealmUser(Resource):
    """Get the local realm user associated with the specified ID.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllLocalRealmUser` (GET (list))
    - `getLocalRealmUser` (GET)
    - `createMultipleLocalRealmUser` (CREATE)
    - `updateLocalRealmUser` (UPDATE)
    - `deleteLocalRealmUser` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To filter users by realm, use `realm:{realmUUID}` To filter users by name, use `name:{name}`
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Boolean indicating whether this is a bulk operation.
    """
    PATH = '/object/localrealmusers/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
