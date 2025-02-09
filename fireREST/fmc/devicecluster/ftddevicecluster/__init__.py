from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_640, API_RELEASE_710
from fireREST.fmc import Connection, Resource
from fireREST.fmc.devicecluster.ftddevicecluster.operational import Operational


class FtdDeviceCluster(Resource):
    PATH = '/deviceclusters/ftddevicecluster/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
    SUPPORTED_PARAMS = ['skip_control_readiness']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.operational = Operational(conn)

    @utils.minimum_version_required(version=API_RELEASE_710)
    def readiness_check(self, data: Dict, skip_control_readiness=None, params=None):
        url = self.url(path='/deviceclusters/ftdclusterreadinesscheck')
        return self.conn.post(url=url, data=data, params=params)
