from fireREST.fmc import Connection
from fireREST.fmc.netmap.host import Host
from fireREST.fmc.netmap.vulnerability import Vulnerability


class NetMap:
    def __init__(self, conn: Connection):
        self.host = Host(conn)
        self.vulnerability = Vulnerability(conn)
