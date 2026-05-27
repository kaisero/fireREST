from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class TimezoneSettings(ChildResource):
    """Retrieves time zone settings policy for particular chassis platform settings policies associated with the ID.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllChassisTimeZoneSetting` (GET (list))
    - `getChassisTimeZoneSetting` (GET)
    - `updateChassisTimeZoneSetting` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'ChassisPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/chassisplatformsettingspolicies/{uuid}'
    PATH = '/policy/chassisplatformsettingspolicies/{container_uuid}/timezonesettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
