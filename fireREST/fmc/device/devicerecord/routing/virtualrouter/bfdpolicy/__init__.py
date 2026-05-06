from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import NestedChildResource


class BfdPolicy(NestedChildResource):
    """Retrieves, deletes, creates, or modifies the BFD Policy associated with the specified ID. If no ID is specified for a GET, retrieves list of all BFD Policies.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVrfBFDPolicyModel` (GET (list))
    - `getVrfBFDPolicyModel` (GET)
    - `createVrfBFDPolicyModel` (CREATE)
    - `updateVrfBFDPolicyModel` (UPDATE)
    - `deleteVrfBFDPolicyModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    CHILD_CONTAINER_NAME = 'VirtualRouter'
    CHILD_CONTAINER_PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{child_container_uuid}/bfdpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730
