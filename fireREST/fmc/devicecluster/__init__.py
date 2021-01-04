from fireREST.fmc import Connection
from fireREST.fmc.devicecluster.ftddevicecluster import FtdDeviceCluster


class DeviceCluster:
    def __init__(self, conn: Connection):
        self.ftddevicecluster = FtdDeviceCluster(conn)
