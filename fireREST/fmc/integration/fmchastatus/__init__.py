from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class FmcHaStatus(Resource):
    """Retrieves information about the High Availability status of the Firepower Management Center

    **Tags:** Integration

    **Supported operations:** GET

    **Operation IDs:**

    - `getFMCHAStatus` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/integration/fmchastatuses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
