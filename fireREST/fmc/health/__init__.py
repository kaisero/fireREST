from fireREST.fmc import Connection
from fireREST.fmc.health.alert import Alert
from fireREST.fmc.health.metric import Metric
from fireREST.fmc.health.tunnelstatus import TunnelStatus
from fireREST.fmc.health.tunnelsummary import TunnelSummary


class Health:
    def __init__(self, conn: Connection):
        self.alert = Alert(conn)
        self.metric = Metric(conn)
        self.tunnelstatus = TunnelStatus(conn)
        self.tunnelsummary = TunnelSummary(conn)
