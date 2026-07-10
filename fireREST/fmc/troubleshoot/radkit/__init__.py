from fireREST.fmc import Connection
from fireREST.fmc.troubleshoot.radkit.service import RadKitService


class RadKit:
    def __init__(self, conn: Connection):
        self.service = RadKitService(conn)
