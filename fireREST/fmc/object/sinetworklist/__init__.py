from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class SiNetworkList(Resource):
    """APIs for Security Intelligence network list.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllSINetworkList` (GET (list))
    - `getSINetworkList` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/sinetworklists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
