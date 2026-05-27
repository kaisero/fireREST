from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class Datacenter(Resource):
    """Retrieves list of all the Umbrella data centers.

    **Tags:** Integration

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllUmbrellaDataCenter` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/integration/umbrella/datacenters/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
