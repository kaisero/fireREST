from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class DeviceSettings(Resource):
    """Retrieves or modifies the Device Settings.

    **Tags:** Devices

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllDeviceSettings` (GET (list))
    - `getDeviceSettings` (GET)
    - `updateMultipleDeviceSettings` (UPDATE (bulk))
    - `updateDeviceSettings` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): Enables bulk update on device settings.
    """

    PATH = '/devices/devicesettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
