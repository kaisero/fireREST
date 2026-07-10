from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ExtendedCommunityListOverride(ChildResource):
    """Get the specified override on an Extended Community List.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllExtendedCommunityListOverride` (GET (list))
    - `getExtendedCommunityListOverride` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'ExtendedCommunityList'
    CONTAINER_PATH = '/object/extendedcommunitylists/{uuid}'
    PATH = '/object/extendedcommunitylists/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
