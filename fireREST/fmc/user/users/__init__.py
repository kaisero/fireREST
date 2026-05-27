from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class Users(Resource):
    """Retrieves the list of all users on FMC.

    **Tags:** Users

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllFMCUser` (GET (list))
    - `getFMCUser` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/users/users/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
