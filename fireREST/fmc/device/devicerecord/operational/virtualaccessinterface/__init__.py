from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class VirtualAccessInterface(ChildResource):
    """Retrieves the Virtual Access Interfaces on all the managed Firewall Threat Defenses.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllVirtualAccessInterface` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): The allowed filter is ` dvtiId:{Uuid}` which filters the access interfaces according to their parent DVTI.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/operational/virtualaccessinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
