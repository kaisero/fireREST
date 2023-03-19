from fireREST.fmc import Connection
from fireREST.fmc.troubleshoot.packettracer import PacketTracer


class Troubleshoot:
    def __init__(self, conn: Connection):
        self.packettracer = PacketTracer(conn)
