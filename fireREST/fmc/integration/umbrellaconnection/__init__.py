from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class UmbrellaConnection(Resource):
    """Retrieves Umbrella connection configuration.

    **Tags:** Integration

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllUmbrellaConnection` (GET (list))
    - `getUmbrellaConnection` (GET)
    - `updateUmbrellaConnection` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/integration/umbrellaconnections/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
