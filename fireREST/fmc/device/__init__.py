from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_630, API_RELEASE_720
from fireREST.fmc import Connection, Resource
from fireREST.fmc.device.devicerecord import DeviceRecord
from fireREST.fmc.device.devicesettings import DeviceSettings


class Device(Resource):
    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.devicerecord = DeviceRecord(conn)
        self.devicesettings = DeviceSettings(conn)

    @utils.minimum_version_required(version=API_RELEASE_630)
    def copyconfigrequest(self, data: Dict):
        url = self.url(path='/devices/copyconfigrequests')
        return self.conn.post(url=url, data=data)

    @utils.minimum_version_required(version=API_RELEASE_720)
    def changemanager(self, data: Dict):
        url = self.url(path='/devices/changemanagers')
        return self.conn.post(url=url, data=data)
