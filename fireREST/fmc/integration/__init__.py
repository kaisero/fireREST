from fireREST.fmc import Connection
from fireREST.fmc.integration.cloudeventsconfig import CloudEventsConfig
from fireREST.fmc.integration.cloudregion import CloudRegion
from fireREST.fmc.integration.externallookup import ExternalLookup
from fireREST.fmc.integration.externalstorage import ExternalStorage


class Integration:
    def __init__(self, conn: Connection):
        self.cloudeventsconfig = CloudEventsConfig(conn)
        self.cloudregion = CloudRegion(conn)
        self.externallookup = ExternalLookup(conn)
        self.externalstorage = ExternalStorage(conn)
