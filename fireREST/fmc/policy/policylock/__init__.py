from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class PolicyLock(Resource):
    """Get the shallow lock details of the Policy. Currently only supports Access policies.

    **Tags:** Policy

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getPolicyLock` (GET (list))
    - `createPolicyLock` (CREATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/operational/policylocks'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
