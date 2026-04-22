from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class FlexConfigPolicy(Resource):
    PATH = '/policy/flexconfigpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730

    @utils.minimum_version_required(version=API_RELEASE_730)
    def migrate(self, data: Dict, uuid: str, params=None):
        url = self.url(f'/policy/flexconfigpolicies/{uuid}/migrate')
        return self.conn.post(url=url, data=data, params=params)
