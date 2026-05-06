from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class Realm(Resource):
    """Retrieves the realm object associated with the specified ID. If no ID is specified, retrieves list of all realm objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllRealm` (GET (list))
    - `getRealm` (GET)
    - `createRealm` (CREATE)
    - `updateRealm` (UPDATE)
    - `deleteRealm` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:name;realmType:realmType;enabled:enabled` `name` -- Name of the realm to be queried. May start with ^ to indicate filtering by names starting with, rather than containing. `realmType` -- Type of the realm to be queried. A comma seperated list of realm types. `enabled` -- Either `true` or `false`.
    - `name` (string, optional): Name of the realm to be queried.
    - `realmType` (string, optional): Type of the realm to be queried.
    - `enabled` (string, optional): Either `true` or `false`,
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/realms/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700
