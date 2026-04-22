from fireREST.fmc import Connection
from fireREST.fmc.troubleshoot.packettracer import PacketTracer
from fireREST.fmc.troubleshoot.task import Task


class Troubleshoot:
    def __init__(self, conn: Connection):
        self.packettracer = PacketTracer(conn)
        self.task = Task(conn)
