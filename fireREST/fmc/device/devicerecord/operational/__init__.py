from fireREST.fmc import Connection
from fireREST.fmc.device.devicerecord.operational.command import Command
from fireREST.fmc.device.devicerecord.operational.metric import Metric
from fireREST.fmc.device.devicerecord.operational.virtualaccessinterface import VirtualAccessInterface


class Operational:
    def __init__(self, conn: Connection):
        self.command = Command(conn)
        self.metric = Metric(conn)
        self.virtualaccessinterface = VirtualAccessInterface(conn)
