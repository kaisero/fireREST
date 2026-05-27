from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import Resource


class CommunityList(Resource):
    """Community lists object Read only.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllCommunityList` (GET (list))
    - `getCommunityList` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/communitylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_650
