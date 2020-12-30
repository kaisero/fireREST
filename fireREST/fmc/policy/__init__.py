from fireREST.fmc import Connection
from fireREST.fmc.policy.accesspolicy import AccessPolicy
from fireREST.fmc.policy.filepolicy import FilePolicy

from fireREST.fmc.policy.ftdnatpolicy import FtdNatPolicy
from fireREST.fmc.policy.ftds2svpn import FtdS2sVpn
from fireREST.fmc.policy.intrusionpolicy import IntrusionPolicy
from fireREST.fmc.policy.prefilterpolicy import PrefilterPolicy
from fireREST.fmc.policy.snmpalert import SnmpAlert
from fireREST.fmc.policy.syslogalert import SyslogAlert


class Policy:
    def __init__(self, conn: Connection):
        self.accesspolicy = AccessPolicy(conn)
        self.filepolicy = FilePolicy(conn)
        self.ftdnatpolicy = FtdNatPolicy(conn)
        self.ftds2svpn = FtdS2sVpn(conn)
        self.intrusionpolicy = IntrusionPolicy(conn)
        self.prefilterpolicy = PrefilterPolicy(conn)
        self.snmpalert = SnmpAlert(conn)
        self.syslogalert = SyslogAlert(conn)
