from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class AzureAdRealm(Resource):
    PATH = '/object/azureadrealms/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740

    @utils.minimum_version_required(version=API_RELEASE_740)
    def download(self, uuid: str, data: Dict, params=None):
        url = self.url(f'/object/azureadrealms/{uuid}/download')
        return self.conn.post(url=url, data=data, params=params)

    @utils.minimum_version_required(version=API_RELEASE_740)
    def usersandgroups(self, uuid: str, params=None):
        url = self.url(f'/object/azureadrealms/{uuid}/usersandgroups')
        return self.conn.get(url=url, params=params)
