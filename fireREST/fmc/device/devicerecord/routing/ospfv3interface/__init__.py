from fireREST.defaults import API_RELEASE_660, API_RELEASE_770
from fireREST.fmc import ChildResource


class Ospfv3Interface(ChildResource):
    """Retrieves list of OSPF v3 process. Also, deletes, creates, or modifies the OSPFv3 Interface associated with the specified ID.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllOspfv3InterfacePolicyModel` (GET (list))
    - `getOspfv3InterfacePolicyModel` (GET)
    - `createOspfv3InterfacePolicyModel` (CREATE)
    - `updateOspfv3InterfacePolicyModel` (UPDATE)
    - `deleteOspfv3InterfacePolicyModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ospfv3interfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_770
