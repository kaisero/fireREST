from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource


class Ospfv3Interface(ChildResource):
    """Retrieves list of OSPF v3 process. Also, deletes, creates, or modifies the OSPFv3 Interface associated with the specified ID.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllOspfv3InterfacePolicyModel` (GET (list))
    - `getOspfv3InterfacePolicyModel` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ospfv3interfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
