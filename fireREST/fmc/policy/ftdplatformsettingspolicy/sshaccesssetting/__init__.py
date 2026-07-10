from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import ChildResource


class SshAccessSetting(ChildResource):
    """Retrieves, creates, updates, or deletes SSH access settings for the specified FTD platform settings policy.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSshAccessSetting` (GET (list))
    - `getSshAccessSetting` (GET)
    - `createSshAccessSetting` (CREATE)
    - `updateSshAccessSetting` (UPDATE)
    - `deleteSshAccessSetting` (DELETE)
    """

    CONTAINER_NAME = 'FtdPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/ftdplatformsettingspolicies/{uuid}'
    PATH = '/policy/ftdplatformsettingspolicies/{container_uuid}/sshaccesssettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_770
