from fireREST.fmc import Connection
from fireREST.fmc.health.alert import Alert
from fireREST.fmc.health.metric import Metric


class Health:
    def __init__(self, conn: Connection):
        self.alert = Alert(conn)
        self.metric = Metric(conn)
