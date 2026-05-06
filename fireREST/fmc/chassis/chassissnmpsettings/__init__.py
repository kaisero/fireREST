from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ChassisSnmpSettings(ChildResource):
    """Retrieves SNMP settings policy for particular chassis

    **Tags:** Chassis

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllChassisSnmpSettings` (GET (list))
    - `getChassisSnmpSettings` (GET)
    - `updateChassisSnmpSettings` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/snmpsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
