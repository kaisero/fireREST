from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class InspectorConfig(ChildResource):
    """Retrieves the inspector configuration associated with the specified network analysis policy. The effective behaviour of the inspector configuration can be modified by modifying the inspector override configuration for the specified policy.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getInspectorConfig` (GET (list))

    **Query parameters:**

    - `inspectors` (string, optional): Retrieves only the specified inspectors of the specified network analysis policy. Input is a comma-separated list of inspector names.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'NetworkAnalysisPolicy'
    CONTAINER_PATH = '/policy/networkanalysispolicies/{uuid}'
    PATH = '/policy/networkanalysispolicies/{container_uuid}/inspectorconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
