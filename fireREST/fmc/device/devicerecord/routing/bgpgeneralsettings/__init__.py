from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource


class BgpGeneralSettings(ChildResource):
    """Retrieves BGP general settings associated with the specified device.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllBGPGeneralSettingModel` (GET (list))
    - `getBGPGeneralSettingModel` (GET)
    - `createBGPGeneralSettingModel` (CREATE)
    - `updateBGPGeneralSettingModel` (UPDATE)
    - `deleteBGPGeneralSettingModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/bgpgeneralsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
