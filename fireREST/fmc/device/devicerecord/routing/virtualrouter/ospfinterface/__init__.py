from fireREST.defaults import API_RELEASE_660, API_RELEASE_770
from fireREST.fmc import NestedChildResource


class OspfInterface(NestedChildResource):
    """Retrieves, deletes, creates, or modifies the OSPF Interface associated with the specified ID. Also, retrieves list of all OSPF v2 process.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVrfOspfInterfacePolicyModel` (GET (list))
    - `getVrfOspfInterfacePolicyModel` (GET)
    - `createVrfOspfInterfacePolicyModel` (CREATE)
    - `updateVrfOspfInterfacePolicyModel` (UPDATE)
    - `deleteVrfOspfInterfacePolicyModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    CHILD_CONTAINER_NAME = 'VirtualRouter'
    CHILD_CONTAINER_PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{child_container_uuid}/ospfinterface/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_770
