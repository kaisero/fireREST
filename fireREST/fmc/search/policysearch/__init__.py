from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class PolicySearch(Resource):
    """Search for policies matching specified text or IP address, including values found in policies.

    **Tags:** Search

    **Supported operations:** GET

    **Operation IDs:**

    - `getGlobalPolicySearch` (GET (list))

    **Query parameters:**

    - `filter` (string): Text or IP address used for filtering.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/search/policy'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
