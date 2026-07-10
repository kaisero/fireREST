from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import Resource


class CloudIntegration(Resource):
    """****

    **Tags:** Integration

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllCloudIntegrationStatus` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/integration/cloudintegrations/cloudintegrations'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
