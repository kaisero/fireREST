from fireREST.fmc import Connection, Resource
from fireREST.fmc.deployment.deployabledevice.deployment import Deployment
from fireREST.fmc.deployment.deployabledevice.pendingchanges import PendingChanges


class DeployableDevice(Resource):
    PATH = '/deployment/deployabledevices/{uuid}'
    SUPPORTED_PARAMS = ['group_dependency']
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'

    def __init__(self, conn: Connection):
        self.deployment = Deployment(conn)
        self.pendingchanges = PendingChanges(conn)
        super().__init__(conn)
