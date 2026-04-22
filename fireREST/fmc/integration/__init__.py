from fireREST.fmc import Connection
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


class Integration:
    def __init__(self, conn: Connection):
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
