from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Connection, Resource
from fireREST.fmc.object.extendedcommunitylist.override import ExtendedCommunityListOverride


class ExtendedCommunityList(Resource):
    """Get the Extended Community List associated with the specified ID.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllExtendedCommunityList` (GET (list))
    - `getExtendedCommunityList` (GET)
    - `createExtendedCommunityList` (CREATE)
    - `updateExtendedCommunityList` (UPDATE)
    - `deleteExtendedCommunityList` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): UUID of the target on which the object override is present.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value and `"type:{type}"` to search for specific type of the object.For ExtendedCommunityLists supported types are Standard and Expanded.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/extendedcommunitylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.override = ExtendedCommunityListOverride(conn)
