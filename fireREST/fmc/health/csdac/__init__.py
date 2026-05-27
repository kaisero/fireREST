from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class Csdac(Resource):
    """Retrieves or updates the Cisco Secure Dynamic Attributes Connector status for the device.

    **Tags:** Health

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getCSDACStatus` (GET (list))
    - `createCSDACStatus` (CREATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/health/csdac/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
