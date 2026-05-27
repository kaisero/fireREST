from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import Resource


class CloudRegion(Resource):
    """Retrieves or modifies the cloud region configuration associated with the specified ID. If no ID is specified for a GET, retrieves list of all cloud regions.

    **Tags:** Integration

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllCloudRegion` (GET (list))
    - `getCloudRegion` (GET)
    - `updateCloudRegion` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/integration/cloudregions/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_650
