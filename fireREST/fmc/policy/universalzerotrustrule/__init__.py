from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import ChildResource


class UniversalZeroTrustRule(ChildResource):
    """Retrieves, creates, updates, or deletes rules for the specified universal zero-trust policy.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllUniversalZeroTrustRule` (GET (list))
    - `getUniversalZeroTrustRule` (GET)
    - `createUniversalZeroTrustRule` (CREATE)
    - `updateUniversalZeroTrustRule` (UPDATE)
    - `deleteUniversalZeroTrustRule` (DELETE)
    """

    CONTAINER_NAME = 'UniversalZeroTrustPolicy'
    CONTAINER_PATH = '/policy/universalzerotrustpolicies/{uuid}'
    PATH = '/policy/universalzerotrustpolicies/{container_uuid}/universalzerotrustrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_1000
