from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import NestedChildResource


class PolicyBasedRoute(NestedChildResource):
    """Retrieves, deletes, creates, or modifies the Policy Based Route associated for the specified virtual router. Also, retrieves list of all PBR policy.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVrfPBRPolicyModel` (GET (list))
    - `getVrfPBRPolicyModel` (GET)
    - `createVrfPBRPolicyModel` (CREATE)
    - `updateVrfPBRPolicyModel` (UPDATE)
    - `deleteVrfPBRPolicyModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    CHILD_CONTAINER_NAME = 'VirtualRouter'
    CHILD_CONTAINER_PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    PATH = (
        '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{child_container_uuid}/policybasedroutes/{uuid}'
    )
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
