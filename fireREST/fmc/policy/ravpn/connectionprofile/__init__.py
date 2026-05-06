from fireREST.defaults import API_RELEASE_700, API_RELEASE_720
from fireREST.fmc import ChildResource


class ConnectionProfile(ChildResource):
    """Retrieves Connection Profile data inside a VPN RA Topology.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDRAVpnConnectionProfileModel` (GET (list))
    - `getFTDRAVpnConnectionProfileModel` (GET)
    - `createFTDRAVpnConnectionProfileModel` (CREATE)
    - `updateFTDRAVpnConnectionProfileModel` (UPDATE)
    - `deleteFTDRAVpnConnectionProfileModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/connectionprofiles/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720
