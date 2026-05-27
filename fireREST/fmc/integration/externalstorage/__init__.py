from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class ExternalStorage(Resource):
    """Retrieves, deletes, creates, or modifies the external event storage config.

    **Tags:** Integration

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllExternalStorage` (GET (list))
    - `getExternalStorage` (GET)
    - `updateExternalStorage` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/integration/externalstorage/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_670
