from fireREST.defaults import API_RELEASE_650, API_RELEASE_710
from fireREST.fmc import Resource


class PolicyList(Resource):
    """Retrieves, deletes, creates, or modifies the PolicyList object associated with the specified ID. If no ID is specified for a GET, retrieves list of all PolicyList objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllPolicyList` (GET (list))
    - `getPolicyList` (GET)
    - `createPolicyList` (CREATE)
    - `updatePolicyList` (UPDATE)
    - `deletePolicyList` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/policylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
