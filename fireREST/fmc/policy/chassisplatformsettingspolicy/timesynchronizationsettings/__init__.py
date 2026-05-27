from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class TimeSynchronizationSettings(ChildResource):
    """Retrieves the specified time synchronization settings policy for particular chassis platform settings policies.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllChassisTimeSynchronizationSetting` (GET (list))
    - `getChassisTimeSynchronizationSetting` (GET)
    - `updateChassisTimeSynchronizationSetting` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'ChassisPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/chassisplatformsettingspolicies/{uuid}'
    PATH = '/policy/chassisplatformsettingspolicies/{container_uuid}/timesynchronizationsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
