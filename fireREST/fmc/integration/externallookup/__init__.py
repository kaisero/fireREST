from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import Resource


class ExternalLookup(Resource):
    """Retrieves, deletes, creates, or modifies the external lookup associated with the specified ID. If no ID is specified for a GET, retrieves list of all external lookups.

    **Tags:** Integration

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllExternalLookup` (GET (list))
    - `getExternalLookup` (GET)
    - `createExternalLookup` (CREATE)
    - `updateExternalLookup` (UPDATE)
    - `deleteExternalLookup` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/integration/externallookups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_640
