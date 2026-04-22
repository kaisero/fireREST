from fireREST.fmc import Connection
from fireREST.fmc.license.devicelicense import DeviceLicense
from fireREST.fmc.license.smartlicense import SmartLicense


class License:
    def __init__(self, conn: Connection):
        self.devicelicense = DeviceLicense(conn)
        self.smartlicense = SmartLicense(conn)
