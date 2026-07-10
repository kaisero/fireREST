from fireREST.fmc import Connection
from fireREST.fmc.troubleshoot.cpuprofiler.module import CpuProfilerModule


class CpuProfiler:
    def __init__(self, conn: Connection):
        self.module = CpuProfilerModule(conn)
