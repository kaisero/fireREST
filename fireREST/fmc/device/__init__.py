from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_630, API_RELEASE_720
from fireREST.fmc import Connection, Resource
from fireREST.fmc.device.bulkcommand import BulkCommand
from fireREST.fmc.device.bulkregistration import BulkRegistration
from fireREST.fmc.device.certificate import Certificate
from fireREST.fmc.device.certificatesexportdata import CertificatesExportData
from fireREST.fmc.device.devicerecord import DeviceRecord
from fireREST.fmc.device.devicesettings import DeviceSettings
from fireREST.fmc.device.downloadsamplecsv import DownloadSampleCsv
from fireREST.fmc.device.ltpdevicerecord import LtpDeviceRecord
from fireREST.fmc.device.managecertificate import ManageCertificate


class Device(Resource):
    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.bulkcommand = BulkCommand(conn)
        self.bulkregistration = BulkRegistration(conn)
        self.certificate = Certificate(conn)
        self.certificatesexportdata = CertificatesExportData(conn)
        self.devicerecord = DeviceRecord(conn)
        self.devicesettings = DeviceSettings(conn)
        self.downloadsamplecsv = DownloadSampleCsv(conn)
        self.ltpdevicerecord = LtpDeviceRecord(conn)
        self.managecertificate = ManageCertificate(conn)

    @utils.minimum_version_required(version=API_RELEASE_630)
    def copyconfigrequest(self, data: Dict):
        url = self.url(path='/devices/copyconfigrequests')
        return self.conn.post(url=url, data=data)

    @utils.minimum_version_required(version=API_RELEASE_720)
    def changemanager(self, data: Dict):
        url = self.url(path='/devices/changemanagers')
        return self.conn.post(url=url, data=data)
