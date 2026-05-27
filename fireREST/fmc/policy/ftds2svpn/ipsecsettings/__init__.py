from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import ChildResource


class IpsecSettings(ChildResource):
    """Retrieves IPSec Proposal settings inside a VPN Site To Site Topology.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllVpnIPSecSettings` (GET (list))
    - `getVpnIPSecSettings` (GET)
    - `updateVpnIPSecSettings` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'FtdS2sVpn'
    CONTAINER_PATH = '/policy/ftds2svpns/{uuid}'
    PATH = '/policy/ftds2svpns/{container_uuid}/ipsecsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
