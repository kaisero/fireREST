from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import ChildResource


class AdvancedLoggingSetting(ChildResource):
    """Retrieves or updates advanced logging settings for the specified access policy.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllAdvancedLoggingSetting` (GET (list))
    - `getAdvancedLoggingSetting` (GET)
    - `updateAdvancedLoggingSetting` (UPDATE)
    """

    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/advancedloggingsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
