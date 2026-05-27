from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import NestedChildResource


class Bgp(NestedChildResource):
    """Retrieves list of all BGP (ipv4 and ipv6) associated with the specified device for specified vrf.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVrfBGPIPvAddressFamilyModel` (GET (list))
    - `getVrfBGPIPvAddressFamilyModel` (GET)
    - `createVrfBGPIPvAddressFamilyModel` (CREATE)
    - `updateVrfBGPIPvAddressFamilyModel` (UPDATE)
    - `deleteVrfBGPIPvAddressFamilyModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    CHILD_CONTAINER_NAME = 'VirtualRouter'
    CHILD_CONTAINER_PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{child_container_uuid}/bgp/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
