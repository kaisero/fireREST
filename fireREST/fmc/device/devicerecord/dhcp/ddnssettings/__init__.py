from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class DdnsSettings(ChildResource):
    """Retrieves or modifies the DDNS policy associated with the specified container/device Id

    **Tags:** Devices

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllDeviceDDNSSettingModel` (GET (list))
    - `getDeviceDDNSSettingModel` (GET)
    - `updateDeviceDDNSSettingModel` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/dhcp/ddnssettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
