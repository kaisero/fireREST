from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.networkanalysispolicy.inspectorconfig import InspectorConfig
from fireREST.fmc.policy.networkanalysispolicy.inspectoroverrideconfig import InspectorOverrideConfig


class NetworkAnalysisPolicy(Resource):
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
