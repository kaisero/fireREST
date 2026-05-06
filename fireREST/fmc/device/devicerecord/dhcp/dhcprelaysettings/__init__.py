from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class DhcpRelaySettings(ChildResource):
    """Retrieves or modifies the Device DHCP Relay associated with the specified container/device Id

    **Tags:** Devices

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllDeviceDHCPRelaySettings` (GET (list))
    - `getDeviceDHCPRelaySettings` (GET)
    - `updateDeviceDHCPRelaySettings` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/dhcp/dhcprelaysettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
