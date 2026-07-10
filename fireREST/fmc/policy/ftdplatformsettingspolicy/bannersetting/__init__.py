from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import ChildResource


class BannerSetting(ChildResource):
    """Retrieves or updates banner settings for the specified FTD platform settings policy.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllBannerSetting` (GET (list))
    - `getBannerSetting` (GET)
    - `updateBannerSetting` (UPDATE)
    """

    CONTAINER_NAME = 'FtdPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/ftdplatformsettingspolicies/{uuid}'
    PATH = '/policy/ftdplatformsettingspolicies/{container_uuid}/bannersettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
