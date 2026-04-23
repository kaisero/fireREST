from fireREST.fmc import Connection
from fireREST.fmc.deployment.deployabledevice import DeployableDevice
from fireREST.fmc.deployment.deploymentrequest import DeploymentRequest
from fireREST.fmc.deployment.jobhistory import JobHistory
from fireREST.fmc.deployment.pendingchangesrequest import PendingChangesRequest
from fireREST.fmc.deployment.rollbackrequest import RollbackRequest


class Deployment:
    def __init__(self, conn: Connection):
        self.deployabledevice = DeployableDevice(conn)
        self.deploymentrequest = DeploymentRequest(conn)
        self.jobhistory = JobHistory(conn)
        self.pendingchangesrequest = PendingChangesRequest(conn)
        self.rollbackrequest = RollbackRequest(conn)
