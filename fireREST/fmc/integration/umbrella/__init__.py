from fireREST.fmc import Connection
from fireREST.fmc.integration.umbrella.datacenter import Datacenter
from fireREST.fmc.integration.umbrella.tunneldeployment import TunnelDeployment


class Umbrella:
    def __init__(self, conn: Connection):
        self.datacenter = Datacenter(conn)
        self.tunneldeployment = TunnelDeployment(conn)
