from fireREST.fmc import Connection
from fireREST.fmc.device.devicerecord.operational.command import Command
from fireREST.fmc.device.devicerecord.operational.metric import Metric


class Operational:
    def __init__(self, conn: Connection):

        self.command = Command(conn)
        self.metric = Metric(conn)
