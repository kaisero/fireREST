from fireREST import utils
from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import Resource


class TunnelSummary(Resource):
    """Retrieves aggregated summary of tunnel status for S2S VPN on all managed Firewall Threat Defenses.

    **Tags:** Health

    **Supported operations:** GET

    **Operation IDs:**

    - `getTunnelSummary` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): The allowed filters are `"vpnTopologyId:{uuid}"` which filters the tunnel summary by S2S VPN Topology id, `"deviceId:{UUID}"` which filters the tunnel summary by Device id and groupBy `"groupBy:Topology|Device"` which groups tunnel summary by Topology or Device.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/health/tunnelsummaries/{uuid}'
    SUPPORTED_FILTERS = ['device_id', 'group_by', 'vpn_topology_id']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710

    @utils.support_params
    def get(self, device_id=None, group_by=None, vpn_topology_id=None, params=None):
        return super().get(params=params)
