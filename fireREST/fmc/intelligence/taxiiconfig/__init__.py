from fireREST.fmc import Connection
from fireREST.fmc.intelligence.taxiiconfig.collection import Collection
from fireREST.fmc.intelligence.taxiiconfig.discoveryinfo import DiscoveryInfo


class TaxiiConfig:
    def __init__(self, conn: Connection):
        self.collection = Collection(conn)
        self.discoveryinfo = DiscoveryInfo(conn)
