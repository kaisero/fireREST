from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class RaVpnSession(Resource):
    PATH = '/health/ravpnsessions/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730

    @utils.minimum_version_required(version=API_RELEASE_730)
    def terminate(self, data: Dict, params=None):
        url = self.url('/health/ravpnsessions/operational/terminateravpnsessions')
        return self.conn.post(url=url, data=data, params=params)
