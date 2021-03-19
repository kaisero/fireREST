from fireREST.fmc import Connection, Resource
from fireREST.fmc.devicehapair.ftddevicehapair.monitoredinterface import MonitoredInterface
from fireREST.fmc.devicehapair.ftddevicehapair.failoverinterfacemacaddressconfig import (
    FailoverInterfaceMacAddressConfig,
)


class FtdHAPair(Resource):
    PATH = '/devicehapairs/ftddevicehapairs/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.2.3'
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.2.3'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.2.3'
    SUPPORTED_PARAMS = ['name']

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.failoverinterfacemacaddressconfig = FailoverInterfaceMacAddressConfig(conn)
        self.monitoredinterface = MonitoredInterface(conn)
