from fireREST.defaults import API_RELEASE_640, API_RELEASE_630
from fireREST.fmc import Resource


class TunnelTag(Resource):
    """Retrieves the tunnel tag object associated with the specified ID. If no ID is specified, retrieves list of all tunnel tag objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllTunnelTags` (GET (list))
    - `getTunnelTags` (GET)
    - `createMultipleTunnelTags` (CREATE)
    - `updateTunnelTags` (UPDATE)
    - `deleteTunnelTags` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk object operations. Only bulk POST is currently supported for tunnel tags. Allowed values are true and false.
    """
    PATH = '/object/tunneltags/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_640
