from fireREST.fmc import Connection
from fireREST.fmc.troubleshoot.cpuprofiler import CpuProfiler
from fireREST.fmc.troubleshoot.device import Device
from fireREST.fmc.troubleshoot.packettracer import PacketTracer
from fireREST.fmc.troubleshoot.radkit import RadKit
from fireREST.fmc.troubleshoot.snortprofiler import SnortProfiler
from fireREST.fmc.troubleshoot.task import Task


class Troubleshoot:
    def __init__(self, conn: Connection):
        self.cpuprofiler = CpuProfiler(conn)
        self.device = Device(conn)
        self.packettracer = PacketTracer(conn)
        self.radkit = RadKit(conn)
        self.snortprofiler = SnortProfiler(conn)
        self.task = Task(conn)
