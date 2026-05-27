from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class Task(Resource):
    NAMESPACE = 'troubleshoot'
    PATH = '/task'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720

    @utils.minimum_version_required(version=API_RELEASE_720)
    def create(self, data: Dict, params=None):
        url = self.url(self.PATH)
        return self.conn.post(url=url, data=data, params=params)
