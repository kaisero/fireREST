from fireREST.defaults import API_RELEASE_660, API_RELEASE_710
from fireREST.fmc import Resource


class StandardAccessList(Resource):
    """Retrieves, deletes, creates, or modifies the Standard Access List associated with the specified ID. If no ID is specified, retrieves list of all Standard Access List.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllStandardACL` (GET (list))
    - `getStandardACL` (GET)
    - `createStandardACL` (CREATE)
    - `updateStandardACL` (UPDATE)
    - `deleteStandardACL` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/standardaccesslists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
