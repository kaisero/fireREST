from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ApplicationGroup(ChildResource):
    """Retrieves the Zero Trust Application Groups associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllZeroTrustApplicationGroup` (GET (list))
    - `getZeroTrustApplicationGroup` (GET)
    - `createZeroTrustApplicationGroup` (CREATE)
    - `updateZeroTrustApplicationGroup` (UPDATE)
    - `deleteZeroTrustApplicationGroup` (DELETE)

    **Query parameters:**

    - `ignoreWarning` (boolean, optional): Shows any warnings when deleting a zero trust application group policy, if set to false. If not specified, value is set to true and warnings are ignored. Allowed values are true and false.
    - `filter` (string, optional): To filter policies.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'ZeroTrustPolicy'
    CONTAINER_PATH = '/policy/zerotrustpolicies/{uuid}'
    PATH = '/policy/zerotrustpolicies/{container_uuid}/applicationgroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
