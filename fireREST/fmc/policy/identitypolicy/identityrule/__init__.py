from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import ChildResource


class IdentityRule(ChildResource):
    """Get the identity policy rule associated with the specified UUID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIdentityPolicyRule` (GET (list))
    - `getIdentityPolicyRule` (GET)
    - `createIdentityPolicyRule` (CREATE)
    - `updateIdentityPolicyRule` (UPDATE)
    - `deleteIdentityPolicyRule` (DELETE)

    **Query parameters:**

    - `intoCategory` (string, optional): UUID of the identity policy category to which the rule will be added.
    - `aboveRule` (string, optional): UUID of the identity policy rule above which the rule will be added.
    - `belowRule` (string, optional): UUID of the identity policy rule below which the rule will be added.
    - `filter` (string, optional): Format of the filter should be `name:{rule_name}` or `ids:{id1,id2,...}`.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'IdentityPolicy'
    CONTAINER_PATH = '/policy/identitypolicies/{uuid}'
    PATH = '/policy/identitypolicies/{container_uuid}/identityrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_1000
