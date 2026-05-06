from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class IpsecAdvancedSettings(ChildResource):
    """Retrieves IPSec Advance Setting inside a VPN RA Topology.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllFTDRAVpnIPSecIKEv2AdvanceSettingsModel` (GET (list))
    - `getFTDRAVpnIPSecIKEv2AdvanceSettingsModel` (GET)
    - `updateFTDRAVpnIPSecIKEv2AdvanceSettingsModel` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/ipsecadvancedsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
