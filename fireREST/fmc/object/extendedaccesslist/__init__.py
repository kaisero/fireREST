from fireREST.defaults import API_RELEASE_630, API_RELEASE_710
from fireREST.fmc import Resource


class ExtendedAccessList(Resource):
    """Retrieves, deletes, creates, or modifies the Extended Access List associated with the specified ID. If no ID is specified, retrieves list of all Extended Access List.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllExtendedAccessListModel` (GET (list))
    - `getExtendedAccessListModel` (GET)
    - `createExtendedAccessListModel` (CREATE)
    - `updateExtendedAccessListModel` (UPDATE)
    - `deleteExtendedAccessListModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/extendedaccesslists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
