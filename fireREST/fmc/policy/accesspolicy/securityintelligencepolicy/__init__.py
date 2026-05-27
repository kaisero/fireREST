from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class SecurityIntelligencePolicy(ChildResource):
    """Retrieves the security intelligence policy associated with the specified Access Policy.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllAccessPolicySecurityIntelligencePolicy` (GET (list))
    - `getAccessPolicySecurityIntelligencePolicy` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/securityintelligencepolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
