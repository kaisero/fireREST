from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import ChildResource


class InheritanceSettings(ChildResource):
    """Retrieves the inheritance settings associated with specified Access Policy.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllAccessPolicyInheritanceSetting` (GET (list))
    - `getAccessPolicyInheritanceSetting` (GET)
    - `updateAccessPolicyInheritanceSetting` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/inheritancesettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_650
