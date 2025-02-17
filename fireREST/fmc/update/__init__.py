from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_630, API_RELEASE_670, API_RELEASE_710
from fireREST.fmc import Resource
from fireREST.fmc.update.upgradepackage import UpgradePackage


class Update(Resource):
    NAMESPACE = 'platform'
    PATH = '/updates/{uuid}'

    def __init__(self, conn):
        super().__init__(conn)

        self.upgradepackage = UpgradePackage(conn)

    @utils.minimum_version_required(version=API_RELEASE_670)
    def cancel(self, data: Dict):
        url = self.url(path='/updates/cancelupgrades')
        return self.conn.post(url=url, data=data)

    @utils.minimum_version_required(version=API_RELEASE_670)
    def retry(self, data: Dict):
        url = self.url(path='/updates/retryupgrades')
        return self.conn.post(url=url, data=data)

    @utils.minimum_version_required(version=API_RELEASE_710)
    def revert(self, data: Dict):
        url = self.url(path='/updates/revertupgrades')
        return self.conn.post(url=url, data=data)

    @utils.minimum_version_required(version=API_RELEASE_630)
    def upgrade(self, data: Dict):
        url = self.url(path='/updates/upgrades')
        return self.conn.post(url=url, data=data)
