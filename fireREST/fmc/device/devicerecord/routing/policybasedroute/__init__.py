from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import ChildResource


class PolicyBasedRoute(ChildResource):
    """Retrieves, deletes, creates, or modifies Policy Based Route.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllPBRPolicyModel` (GET (list))
    - `getPBRPolicyModel` (GET)
    - `createMultiplePBRPolicyModel` (CREATE)
    - `updatePBRPolicyModel` (UPDATE)
    - `deletePBRPolicyModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for Policy Based Route.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/policybasedroutes/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
