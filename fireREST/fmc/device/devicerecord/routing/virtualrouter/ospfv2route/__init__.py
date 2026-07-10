from fireREST.defaults import API_RELEASE_660, API_RELEASE_770
from fireREST.fmc import NestedChildResource


class Ospfv2Route(NestedChildResource):
    """Retrieves, deletes, creates, or modifies the OSPFV2 associated with the specified ID. Also, retrieves list of all OSPF v2 process.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVrfOspfPolicyModel` (GET (list))
    - `getVrfOspfPolicyModel` (GET)
    - `createVrfOspfPolicyModel` (CREATE)
    - `updateVrfOspfPolicyModel` (UPDATE)
    - `deleteVrfOspfPolicyModel` (DELETE)

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
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_770
