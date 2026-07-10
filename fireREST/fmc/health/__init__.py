from fireREST.fmc import Connection
from fireREST.fmc.health.aggregatemetric import AggregateMetric
from fireREST.fmc.health.alert import Alert
from fireREST.fmc.health.event import Event
from fireREST.fmc.health.metric import Metric
from fireREST.fmc.health.pathmonitoredinterface import PathMonitoredInterface
from fireREST.fmc.health.ravpngateway import RaVpnGateway
from fireREST.fmc.health.ravpnsession import RaVpnSession
from fireREST.fmc.health.tunnelstatus import TunnelStatus
from fireREST.fmc.health.tunnelsummary import TunnelSummary


class Health:
    def __init__(self, conn: Connection):
        self.aggregatemetric = AggregateMetric(conn)
        self.alert = Alert(conn)
        self.event = Event(conn)
        self.metric = Metric(conn)
        self.pathmonitoredinterface = PathMonitoredInterface(conn)
        self.ravpngateway = RaVpnGateway(conn)
        self.ravpnsession = RaVpnSession(conn)
        self.tunnelstatus = TunnelStatus(conn)
        self.tunnelsummary = TunnelSummary(conn)
