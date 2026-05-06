from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class ApplicationTag(Resource):
    """Retrieves the application tag object associated with the specified ID. If no ID is specified, retrieves list of all application tag objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllApplicationTag` (GET (list))
    - `getApplicationTag` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/applicationtags/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
