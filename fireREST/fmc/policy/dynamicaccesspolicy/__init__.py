from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class DynamicAccessPolicy(Resource):
    """Retrieves the Dynamic Access Policy.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDynamicAccessPolicy` (GET (list))
    - `getDynamicAccessPolicy` (GET)
    - `createDynamicAccessPolicy` (CREATE)
    - `updateDynamicAccessPolicy` (UPDATE)
    - `deleteDynamicAccessPolicy` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/dynamicaccesspolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700
