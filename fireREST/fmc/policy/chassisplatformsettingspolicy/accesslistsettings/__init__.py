from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class AccessListSettings(ChildResource):
    """Retrieves Access List policies for a particular Chassis Platform Settings Policy from the Management Center.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllChassisAccessListSetting` (GET (list))
    - `getChassisAccessListSetting` (GET)
    - `updateChassisAccessListSetting` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'ChassisPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/chassisplatformsettingspolicies/{uuid}'
    PATH = '/policy/chassisplatformsettingspolicies/{container_uuid}/accesslistsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
