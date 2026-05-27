from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ChassisInterfaceEvent(ChildResource):
    """Retrieves list of all netmod events on the device.

    **Tags:** Chassis

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getChassisInterfaceEvent` (GET (list))
    - `createChassisInterfaceEvent` (CREATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/chassisinterfaceevents/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
