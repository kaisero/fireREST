from fireREST.fmc import Resource
from fireREST.fmc.update.upgradepackage.applicabledevice import ApplicableDevice


class UpgradePackage(Resource):
    NAMESPACE = 'platform'
    PATH = '/updates/upgradepackages/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.3.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.3.0'

    def __init__(self, conn):
        super().__init__(conn)

        self.applicabledevice = ApplicableDevice(conn)
