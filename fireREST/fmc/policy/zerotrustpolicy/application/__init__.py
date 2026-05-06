from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class Application(ChildResource):
    """Retrieves the Zero Trust Applications associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllZeroTrustApplication` (GET (list))
    - `getZeroTrustApplication` (GET)
    - `createZeroTrustApplication` (CREATE)
    - `updateMultipleZeroTrustApplication` (UPDATE (bulk))
    - `updateZeroTrustApplication` (UPDATE)
    - `deleteMultipleZeroTrustApplication` (DELETE (bulk))
    - `deleteZeroTrustApplication` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To filter policies.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): Required parameter, should be always set to `true`
    - `partialUpdate` (boolean, optional): This field specifies whether to change the entire object or only certain attributes of it. When its value is false the whole object will change, and if the value is true then only the attributes that are specified will change. The default value of this field is false.
    """
    CONTAINER_NAME = 'ZeroTrustPolicy'
    CONTAINER_PATH = '/policy/zerotrustpolicies/{uuid}'
    PATH = '/policy/zerotrustpolicies/{container_uuid}/applications/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
