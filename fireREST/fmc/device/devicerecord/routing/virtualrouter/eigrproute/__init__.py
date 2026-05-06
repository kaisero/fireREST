from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import NestedChildResource


class EigrpRoute(NestedChildResource):
    """Retrieves, deletes, creates, or modifies the EIGRP associated for a specified virtual router with the specified ID. Also, retrieves list of all EIGRP.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVrfEigrpPolicyModel` (GET (list))
    - `getVrfEigrpPolicyModel` (GET)
    - `createVrfEigrpPolicyModel` (CREATE)
    - `updateVrfEigrpPolicyModel` (UPDATE)
    - `deleteVrfEigrpPolicyModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    CHILD_CONTAINER_NAME = 'VirtualRouter'
    CHILD_CONTAINER_PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{child_container_uuid}/eigrproutes/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720
