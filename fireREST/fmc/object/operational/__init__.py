from fireREST.fmc import Connection
from fireREST.fmc.object.operational.usage import Usage


class Operational:
    def __init__(self, conn: Connection):
        self.usage = Usage(conn)
