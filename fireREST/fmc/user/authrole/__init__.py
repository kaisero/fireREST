from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class AuthRole(Resource):
    """Retrieves the list of all existing user roles in the system.

    **Tags:** Users

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllAuthRoles` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/users/authroles/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
