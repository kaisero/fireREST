from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class InspectorOverrideConfig(ChildResource):
    """Retrieves the inspector override configuration associated with the specified policy. An inspector override allows the user to modify behaviour specified in the base policys inspector configuration.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getInspectorOverrideConfig` (GET (list))
    - `updateInspectorOverrideConfig` (UPDATE (bulk))
    - `updateInspectorOverrideConfig` (UPDATE)

    **Query parameters:**

    - `inspectors` (string, optional): Retrieves only the specified inspectors of the specified network analysis policy. Input is a comma-separated list of inspector names.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'NetworkAnalysisPolicy'
    CONTAINER_PATH = '/policy/networkanalysispolicies/{uuid}'
    PATH = '/policy/networkanalysispolicies/{container_uuid}/inspectoroverrideconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
