from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import ChildResource


class Endpoint(ChildResource):
    """Retrieves a specific Endpoint associated with the specified ID inside a VPN Site To Site Topology.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVpnEndpoint` (GET (list))
    - `getVpnEndpoint` (GET)
    - `createVpnEndpoint` (CREATE)
    - `updateVpnEndpoint` (UPDATE)
    - `deleteVpnEndpoint` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'FtdS2sVpn'
    CONTAINER_PATH = '/policy/ftds2svpns/{uuid}'
    PATH = '/policy/ftds2svpns/{container_uuid}/endpoints/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
