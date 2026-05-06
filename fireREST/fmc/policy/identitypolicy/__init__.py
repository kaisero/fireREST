from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class IdentityPolicy(Resource):
    """Retrieves the Identity Policy associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllIdentityPolicy` (GET (list))
    - `getIdentityPolicy` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/identitypolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
