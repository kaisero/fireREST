from typing import Dict

from fireREST import utils
from fireREST.fmc import Resource
from fireREST.fmc.update.upgradepackage import UpgradePackage


class Update(Resource):
    NAMESPACE = 'platform'
    PATH = '/updates/{uuid}'

    def __init__(self, conn):
        super().__init__(conn)

        self.upgradepackage = UpgradePackage(conn)

    @utils.minimum_version_required(version='6.7.0')
    def cancel(self, data: Dict):
        url = self.url(path='/updates/cancelupgrades')
        return self.conn.post(url=url, data=data)

    @utils.minimum_version_required(version='6.7.0')
    def retry(self, data: Dict):
        url = self.url(path='/updates/retryupgrades')
        return self.conn.post(url=url, data=data)

    @utils.minimum_version_required(version='6.3.0')
    def upgrade(self, data: Dict):
        url = self.url(path='/updates/upgrades')
        return self.conn.post(url=url, data=data)
