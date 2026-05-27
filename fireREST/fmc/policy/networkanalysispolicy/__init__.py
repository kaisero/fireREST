from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.networkanalysispolicy.inspectorconfig import InspectorConfig
from fireREST.fmc.policy.networkanalysispolicy.inspectoroverrideconfig import InspectorOverrideConfig


class NetworkAnalysisPolicy(Resource):
    """Retrieves the network analysis policy associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSnort3NetworkAnalysisPolicy` (GET (list))
    - `getSnort3NetworkAnalysisPolicy` (GET)
    - `createSnort3NetworkAnalysisPolicy` (CREATE)
    - `updateSnort3NetworkAnalysisPolicy` (UPDATE)
    - `deleteSnort3NetworkAnalysisPolicy` (DELETE)

    **Query parameters:**

    - `replicateInspectionMode` (string, optional): Flag to replicate inspection mode from Snort 3 version to Snort 2 version.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/networkanalysispolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.inspectorconfig = InspectorConfig(conn)
        self.inspectoroverrideconfig = InspectorOverrideConfig(conn)
