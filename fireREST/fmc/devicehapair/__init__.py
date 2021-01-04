from fireREST.fmc import Connection
from fireREST.fmc.devicehapair.ftddevicehapair import FtdHAPair


class DeviceHAPair:
    def __init__(self, conn: Connection):
        self.ftdhapair = FtdHAPair(conn)
