from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class PolicyAssignment(Resource):
    """Retrieves, creates, or modifies the policy assignments to target devices associated with the specified ID. If no ID is specified, retrieves list of all policy assignments to target devices.

    **Tags:** Policy Assignments

    **Supported operations:** GET, CREATE, UPDATE

    **Operation IDs:**

    - `getAllPolicyAssignment` (GET (list))
    - `getPolicyAssignment` (GET)
    - `createPolicyAssignment` (CREATE)
    - `updatePolicyAssignment` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/assignment/policyassignments/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
