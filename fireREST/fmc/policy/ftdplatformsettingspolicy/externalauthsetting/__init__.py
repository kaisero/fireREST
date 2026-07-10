from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import ChildResource


class ExternalAuthSetting(ChildResource):
    """Retrieves or updates external authentication settings for the specified FTD platform settings policy.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllExternalAuthSetting` (GET (list))
    - `getExternalAuthSetting` (GET)
    - `updateExternalAuthSetting` (UPDATE)
    """

    CONTAINER_NAME = 'FtdPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/ftdplatformsettingspolicies/{uuid}'
    PATH = '/policy/ftdplatformsettingspolicies/{container_uuid}/externalauthsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
