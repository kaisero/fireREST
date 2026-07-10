from fireREST.fmc import Connection
from fireREST.fmc.troubleshoot.snortprofiler.rule import SnortProfilerRule


class SnortProfiler:
    def __init__(self, conn: Connection):
        self.rule = SnortProfilerRule(conn)
