from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class TunnelDetails(ChildResource):
    """Retrieves tunnel details for Site-to-Site VPN by executing show commands on managed peers.

    **Tags:** Health

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllTunnelDetail` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'TunnelStatus'
    CONTAINER_PATH = '/health/tunnelstatuses/{uuid}'
    PATH = '/health/tunnelstatuses/{container_uuid}/tunneldetails/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
