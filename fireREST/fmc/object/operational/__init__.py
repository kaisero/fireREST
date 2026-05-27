from fireREST.fmc import Connection
from fireREST.fmc.object.operational.findoverlaps import FindOverlaps
from fireREST.fmc.object.operational.usage import Usage


class Operational:
    def __init__(self, conn: Connection):
        self.findoverlaps = FindOverlaps(conn)
        self.usage = Usage(conn)
