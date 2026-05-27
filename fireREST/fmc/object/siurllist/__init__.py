from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import Resource


class SiUrlList(Resource):
    """Retrieves, creates, deletes or modifies the Security Intelligence URL List object associated with the specified ID. If no ID is specified, retrieves list of all Security Intelligence URL List objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSIURLList` (GET (list))
    - `getSIURLList` (GET)
    - `createSIURLList` (CREATE)
    - `updateSIURLList` (UPDATE)
    - `deleteSIURLList` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/siurllists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
