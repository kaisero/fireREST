from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class IpsecCryptoMap(ChildResource):
    """Get the IPSec Crypto Map Setting associated with the specified ID inside a remote access VPN Topology.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllFTDRAVpnIPSecCryptoMapModel` (GET (list))
    - `getFTDRAVpnIPSecCryptoMapModel` (GET)
    - `updateFTDRAVpnIPSecCryptoMapModel` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/ipseccryptomaps/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
