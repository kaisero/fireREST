from fireREST.defaults import API_RELEASE_700, API_RELEASE_610
from fireREST.fmc import Resource


class ApplicationFilter(Resource):
    """Retrieves, deletes, creates, or modifies the application filter object associated with the specified ID. If no ID is specified, retrieves list of all application filter objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllApplicationFilter` (GET (list))
    - `getApplicationFilter` (GET)
    - `createApplicationFilter` (CREATE)
    - `updateApplicationFilter` (UPDATE)
    - `deleteApplicationFilter` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/applicationfilters/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700
