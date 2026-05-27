from fireREST.fmc import Connection
from fireREST.fmc.systemconfiguration.changemanagementconfig import ChangeManagementConfig
from fireREST.fmc.systemconfiguration.remotemanagementaccess import RemoteManagementAccess


class SystemConfiguration:
    def __init__(self, conn: Connection):
        self.changemanagementconfig = ChangeManagementConfig(conn)
        self.remotemanagementaccess = RemoteManagementAccess(conn)
