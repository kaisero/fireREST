from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource


class OspfInterface(ChildResource):
    """Retrieves, deletes, creates, or modifies the OSPF Interface associated with the specified ID. Also, retrieves list of all OSPF v2 process. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllOspfInterfacePolicyModel` (GET (list))
    - `getOspfInterfacePolicyModel` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ospfinterface/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
