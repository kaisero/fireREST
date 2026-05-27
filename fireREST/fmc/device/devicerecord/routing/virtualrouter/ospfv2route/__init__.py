from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import NestedChildResource


class Ospfv2Route(NestedChildResource):
    """Retrieves, deletes, creates, or modifies the OSPFV2 associated with the specified ID. Also, retrieves list of all OSPF v2 process.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllVrfOspfPolicyModel` (GET (list))
    - `getVrfOspfPolicyModel` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    CHILD_CONTAINER_NAME = 'VirtualRouter'
    CHILD_CONTAINER_PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{child_container_uuid}/ospfv2routes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
