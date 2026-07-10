from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import ChildResource


class UniversalZeroTrustSetting(ChildResource):
    """Retrieves or updates universal zero-trust settings for the specified device record.

    **Tags:** Devices

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllUniversalZeroTrustSetting` (GET (list))
    - `getUniversalZeroTrustSetting` (GET)
    - `updateUniversalZeroTrustSetting` (UPDATE)
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/universalzerotrustsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
