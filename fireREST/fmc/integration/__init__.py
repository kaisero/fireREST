from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Connection, Resource
from fireREST.fmc.integration.cdfmcsnapshot import CdfmcSnapshot
from fireREST.fmc.integration.cloudeventsconfig import CloudEventsConfig
from fireREST.fmc.integration.cloudregion import CloudRegion
from fireREST.fmc.integration.ebssnapshot import EbsSnapshot
from fireREST.fmc.integration.externallookup import ExternalLookup
from fireREST.fmc.integration.externalstorage import ExternalStorage
from fireREST.fmc.integration.fmchastatus import FmcHaStatus
from fireREST.fmc.integration.securexconfig import SecurexConfig
from fireREST.fmc.integration.testumbrellaconnection import TestUmbrellaConnection
from fireREST.fmc.integration.umbrella import Umbrella
from fireREST.fmc.integration.umbrellaconnection import UmbrellaConnection


class Integration(Resource):
    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.cdfmcsnapshot = CdfmcSnapshot(conn)
        self.cloudeventsconfig = CloudEventsConfig(conn)
        self.cloudregion = CloudRegion(conn)
        self.ebssnapshot = EbsSnapshot(conn)
        self.externallookup = ExternalLookup(conn)
        self.externalstorage = ExternalStorage(conn)
        self.fmchastatus = FmcHaStatus(conn)
        self.securexconfig = SecurexConfig(conn)
        self.testumbrellaconnection = TestUmbrellaConnection(conn)
        self.umbrella = Umbrella(conn)
        self.umbrellaconnection = UmbrellaConnection(conn)

    @utils.minimum_version_required(version=API_RELEASE_740)
    def refresh_securex_configs(self, data: Dict):
        url = self.url(path='/integration/operational/refreshsecurexconfigs')
        return self.conn.post(url=url, data=data)
