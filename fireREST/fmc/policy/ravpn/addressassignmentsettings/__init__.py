from fireREST.defaults import API_RELEASE_700, API_RELEASE_720
from fireREST.fmc import ChildResource


class AddressAssignmentSettings(ChildResource):
    """Retrieves Address Assignment Setting inside a VPN RA Topology.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllFTDRAVpnAddressAssignmentSetting` (GET (list))
    - `getFTDRAVpnAddressAssignmentSetting` (GET)
    - `updateFTDRAVpnAddressAssignmentSetting` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/addressassignmentsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
