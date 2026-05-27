from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class VpnTunnelStatus(Resource):
    """Retrieves list of all VPN Tunnel Status.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllVpnTunnelStatusModel` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): The filter criteria for which the details have to be fetched. The following filters are supported - deviceId:{deviceId};vpnTopologyId:{topologyId};deployedStatus:{deployedStatus};status:{status}. User can enter one or many filters.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/vpntunnelstatuses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
