from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class SshServerSettings(ChildResource):
    """Retrieves the SSH server setting policy for particular chassis platform settings policies associated with the ID.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllSshServerSetting` (GET (list))
    - `getSshServerSetting` (GET)
    - `updateSshServerSetting` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'ChassisPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/chassisplatformsettingspolicies/{uuid}'
    PATH = '/policy/chassisplatformsettingspolicies/{container_uuid}/sshserversettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
