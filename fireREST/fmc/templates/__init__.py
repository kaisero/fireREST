from fireREST.fmc import Connection
from fireREST.fmc.templates.devicetemplate import DeviceTemplate
from fireREST.fmc.templates.supporteddevicemodel import SupportedDeviceModel


class Templates:
    def __init__(self, conn: Connection):
        self.devicetemplate = DeviceTemplate(conn)
        self.supporteddevicemodel = SupportedDeviceModel(conn)
