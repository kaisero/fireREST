from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import Resource


class CloudEventsConfig(Resource):
    """Retrieves or modifies the cloud event configuration associated with the specified ID. If no ID is specified for a GET, retrieves a list of the singleton cloud event configuration object.

    **Tags:** Integration

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllCloudEvents` (GET (list))
    - `getCloudEvents` (GET)
    - `updateCloudEvents` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/integration/cloudeventsconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
