from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource
from fireREST.fmc.update.upgradepackage.applicabledevice import ApplicableDevice


class UpgradePackage(Resource):
    NAMESPACE = 'platform'
    PATH = '/updates/upgradepackages/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630

    def __init__(self, conn):
        super().__init__(conn)

        self.applicabledevice = ApplicableDevice(conn)
