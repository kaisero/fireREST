from fireREST.defaults import API_RELEASE_660, API_RELEASE_710
from fireREST.fmc import Resource


class ExpandedCommunityList(Resource):
    """Retrieves, deletes, creates, or modifies the ExpandedCommunityList object associated with the specified ID. If no ID is specified for a GET, retrieves list of all ExpandedCommunityList objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllExpandedCommunityList` (GET (list))
    - `getExpandedCommunityList` (GET)
    - `createExpandedCommunityList` (CREATE)
    - `updateExpandedCommunityList` (UPDATE)
    - `deleteExpandedCommunityList` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/expandedcommunitylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
