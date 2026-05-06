from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class CustomSiIpList(Resource):
    """Retrieves, creates, deletes or modifies the custom Security Intelligence Network List object associated with the specified ID. If no ID is specified, retrieves list of all custom Security Intelligence Network List objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllCustomSIIPList` (GET (list))
    - `getCustomSIIPList` (GET)
    - `createCustomSIIPList` (CREATE)
    - `updateCustomSIIPList` (UPDATE)
    - `deleteCustomSIIPList` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/customsiiplists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
