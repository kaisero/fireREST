from fireREST import utils
from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import Connection, Resource
from fireREST.fmc.health.tunnelstatus.tunneldetails import TunnelDetails


class TunnelStatus(Resource):
    """Retrieves tunnel status for S2S VPN on all managed Firewall Threat Defenses.

    **Tags:** Health

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllTunnelStatus` (GET (list))
    - `getTunnelStatus` (GET)

    **Query parameters:**

    - `filter` (string, optional): The allowed filters are `"vpnTopologyId:{uuid}"` which filters the tunnel statuses by S2S VPN Topology id, `"deviceId:{UUID}"` which filters the tunnel statuses by Device id, `status:{TUNNELUP|TUNNELDOWN|UNKNOWN}` which filters the tunnel statuses by Tunnel Status, `"deployedStatus:{Deployed|Configured|Both}"` which is filters the tunnel status by it's deployed state and `"sortBy{:|<|>}{Topology|Device|Status|LastChange}"`. Filter operators `:` and `<` sorts in ascending order and `>` sorts in descending order.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/health/tunnelstatuses/{uuid}'
    SUPPORTED_FILTERS = ['device_id', 'deployed_status', 'sort_by', 'status', 'vpn_topology_id']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.tunneldetails = TunnelDetails(conn)

    @utils.support_params
    def get(self, device_id=None, deployed_status=None, sort_by=None, status=None, vpn_topology_id=None, params=None):
        return super().get(params=params)
