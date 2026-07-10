from fireREST.fmc import Connection
from fireREST.fmc.updates.contentupdate import ContentUpdate
from fireREST.fmc.updates.contentupdateoperation import ContentUpdateOperation
from fireREST.fmc.updates.deviceupgradeinfo import DeviceUpgradeInfo


class Updates:
    def __init__(self, conn: Connection):
        self.contentupdate = ContentUpdate(conn)
        self.contentupdateoperation = ContentUpdateOperation(conn)
        self.deviceupgradeinfo = DeviceUpgradeInfo(conn)
