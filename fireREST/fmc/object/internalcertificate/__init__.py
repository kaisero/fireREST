from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class InternalCertificate(Resource):
    PATH = '/object/internalcertificates/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730

    @utils.minimum_version_required(version=API_RELEASE_730)
    def validate(self, data: Dict, params=None):
        url = self.url('/object/validatecertfile')
        return self.conn.post(url=url, data=data, params=params)
