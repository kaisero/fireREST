from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class SiNetworkFeed(Resource):
    """APIs for Security Intelligence network feed.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSINetworkFeed` (GET (list))
    - `getSINetworkFeed` (GET)
    - `createSINetworkFeed` (CREATE)
    - `updateSINetworkFeed` (UPDATE)
    - `deleteSINetworkFeed` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/sinetworkfeeds/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
