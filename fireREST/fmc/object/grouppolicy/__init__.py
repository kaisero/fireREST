from fireREST.defaults import API_RELEASE_700, API_RELEASE_720
from fireREST.fmc import Resource


class GroupPolicy(Resource):
    """Defines the group policies for VPN

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllGroupPolicyModel` (GET (list))
    - `getGroupPolicyModel` (GET)
    - `createMultipleGroupPolicyModel` (CREATE)
    - `updateGroupPolicyModel` (UPDATE)
    - `deleteGroupPolicyModel` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for Group Policy object.
    """
    PATH = '/object/grouppolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720
