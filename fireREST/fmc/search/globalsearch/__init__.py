from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class GlobalSearch(Resource):
    """Search for objects and policies matching specified text or IP address.

    **Tags:** Search

    **Supported operations:** GET

    **Operation IDs:**

    - `getGlobalSearch` (GET (list))

    **Query parameters:**

    - `filter` (string): Text or IP address used for filtering.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/search/global'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
