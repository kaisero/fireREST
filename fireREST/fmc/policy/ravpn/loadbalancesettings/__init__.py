from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import ChildResource


class LoadBalanceSettings(ChildResource):
    """Retrieves Load Balance Setting inside a VPN RA Topology.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllFTDRAVpnLoadBalanceSetting` (GET (list))
    - `getFTDRAVpnLoadBalanceSetting` (GET)
    - `updateFTDRAVpnLoadBalanceSetting` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/loadbalancesettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
