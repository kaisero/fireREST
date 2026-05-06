from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class ApplicationProductivity(Resource):
    """Retrieves the application productivity object associated with the specified ID. If no ID is specified, retrieves list of all application productivity objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllApplicationProductivity` (GET (list))
    - `getApplicationProductivity` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/applicationproductivities/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
