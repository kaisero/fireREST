from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class EigrpRoute(ChildResource):
    """Retrieves, deletes, creates, or modifies the EIGRP associated with the specified ID. Also, retrieves list of all EIGRP.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllEigrpPolicyModel` (GET (list))
    - `getEigrpPolicyModel` (GET)
    - `createEigrpPolicyModel` (CREATE)
    - `updateEigrpPolicyModel` (UPDATE)
    - `deleteEigrpPolicyModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/eigrproutes/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720
