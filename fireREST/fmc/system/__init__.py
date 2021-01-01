from fireREST.fmc import Connection
from fireREST.fmc.system.info import Info


class System:
    def __init__(self, conn: Connection):
        self.info = Info(conn)
