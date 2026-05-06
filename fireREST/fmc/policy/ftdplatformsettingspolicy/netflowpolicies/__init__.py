from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class NetflowPolicies(ChildResource):
    """Retrieves the NetFlow Policy.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllNetFlowPolicy` (GET (list))
    - `getNetFlowPolicy` (GET)
    - `updateNetFlowPolicy` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'FtdPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/ftdplatformsettingspolicies/{uuid}'
    PATH = '/policy/ftdplatformsettingspolicies/{container_uuid}/netflowpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
