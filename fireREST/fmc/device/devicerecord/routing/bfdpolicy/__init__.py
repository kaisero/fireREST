from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import ChildResource


class BfdPolicy(ChildResource):
    """Retrieves, deletes, creates, or modifies the BFD Policy associated with the specified ID. If no ID is specified for a GET, retrieves list of all BFD Policies.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllBFDPolicyModel` (GET (list))
    - `getBFDPolicyModel` (GET)
    - `createBFDPolicyModel` (CREATE)
    - `updateBFDPolicyModel` (UPDATE)
    - `deleteBFDPolicyModel` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To filter BFD policies based on hop type, use `hopType:{hopType}`. Supported hop types are Single-Hop and Multi-Hop. To filter BFD policies objects based on IP type, use `ipType:{ipType}`. Supported ip types are v4 and v6.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/bfdpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730
