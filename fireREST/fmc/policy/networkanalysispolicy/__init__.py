import fireREST.fmc.policy.networkanalysispolicy.inspectorconfig
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.networkanalysispolicy.inspectorconfig import InspectorConfig
from fireREST.fmc.policy.networkanalysispolicy.inspectoroverrideconfig import InspectorOverrideConfig


class NetworkAnalysisPolicy(Resource):
    PATH = '/policy/networkanalysispolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '7.0.0'

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.inspectorconfig = InspectorConfig(conn)
        self.inspectoroverrideconfig = InspectorOverrideConfig(conn)
