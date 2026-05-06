from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import ChildResource


class LoggingSettings(ChildResource):
    """Retrieves logging setting associated with the specified access control policy ID and default action ID.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllAccessPolicyLoggingSettingModel` (GET (list))
    - `getAccessPolicyLoggingSettingModel` (GET)
    - `updateAccessPolicyLoggingSettingModel` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/loggingsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
