from fireREST.fmc import Connection
from fireREST.fmc.devicegroup.devicegrouprecord import DeviceGroupRecord


class DeviceGroup:
    def __init__(self, conn: Connection):
        self.devicegrouprecord = DeviceGroupRecord(conn)
