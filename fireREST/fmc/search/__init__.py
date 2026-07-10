from fireREST.fmc import Connection
from fireREST.fmc.search.devicesearch import DeviceSearch
from fireREST.fmc.search.globalsearch import GlobalSearch
from fireREST.fmc.search.objectsearch import ObjectSearch
from fireREST.fmc.search.policysearch import PolicySearch


class Search:
    def __init__(self, conn: Connection):
        self.device = DeviceSearch(conn)
        self.glob = GlobalSearch(conn)
        self.object = ObjectSearch(conn)
        self.policy = PolicySearch(conn)
