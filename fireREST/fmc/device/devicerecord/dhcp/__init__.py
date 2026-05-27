from fireREST.fmc import Connection
from fireREST.fmc.device.devicerecord.dhcp.ddnssettings import DdnsSettings
from fireREST.fmc.device.devicerecord.dhcp.dhcprelaysettings import DhcpRelaySettings
from fireREST.fmc.device.devicerecord.dhcp.dhcpserver import DhcpServer


class Dhcp:
    def __init__(self, conn: Connection):
        self.ddnssettings = DdnsSettings(conn)
        self.dhcprelaysettings = DhcpRelaySettings(conn)
        self.dhcpserver = DhcpServer(conn)
