from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class CustomSiUrlList(Resource):
    """Retrieves, creates, deletes or modifies the custom Security Intelligence URL List object associated with the specified ID. If no ID is specified, retrieves list of all custom Security Intelligence URL List objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllCustomSIURLList` (GET (list))
    - `getCustomSIURLList` (GET)
    - `createCustomSIURLList` (CREATE)
    - `updateCustomSIURLList` (UPDATE)
    - `deleteCustomSIURLList` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/customsiurllists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
