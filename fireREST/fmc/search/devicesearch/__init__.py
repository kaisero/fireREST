from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class DeviceSearch(Resource):
    """Search for devices matching the specified text.

    **Tags:** Search

    **Supported operations:** GET

    **Operation IDs:**

    - `getGlobalDeviceSearch` (GET (list))

    **Query parameters:**

    - `filter` (string): Text used for filtering.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/search/device'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
