from fireREST.fmc import Connection
from fireREST.fmc.system.info.domain import Domain
from fireREST.fmc.system.info.serverversion import ServerVersion


class Info:
    def __init__(self, conn: Connection):
        self.domain = Domain(conn)
        self.serverversion = ServerVersion(conn)
