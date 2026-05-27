from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class RaVpnGateway(Resource):
    """Retrieves the RA VPN Gateway Details. This includes RA VPN Certificate expiry dates, maximum sessions supported.

    **Tags:** Health

    **Supported operations:** GET

    **Operation IDs:**

    - `getRaVpnGateway` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/health/ravpngateways/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
