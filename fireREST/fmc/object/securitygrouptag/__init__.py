from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class SecurityGroupTag(Resource):
    """Retrieves the custom security group tag object associated with the specified ID. If no ID is specified, retrieves list of all custom security group tag objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSecurityGroupTag` (GET (list))
    - `getSecurityGroupTag` (GET)
    - `createSecurityGroupTag` (CREATE)
    - `updateSecurityGroupTag` (UPDATE)
    - `deleteSecurityGroupTag` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/securitygrouptags/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
