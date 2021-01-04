from typing import Dict

from fireREST import utils
from fireREST.fmc import Connection, Resource
from fireREST.fmc.device.devicerecord import DeviceRecord


class Device(Resource):
    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.devicerecord = DeviceRecord(conn)

    @utils.minimum_version_required(version='6.3.0')
    def copyconfigrequest(self, data: Dict):
        url = self.url(path='/devices/copyconfigrequests')
        return self.conn.post(url=url, data=data)
