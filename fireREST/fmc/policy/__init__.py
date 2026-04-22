from fireREST.fmc import Connection
from fireREST.fmc.policy.accesspolicy import AccessPolicy
from fireREST.fmc.policy.dnspolicy import DnsPolicy
from fireREST.fmc.policy.dynamicaccesspolicy import DynamicAccessPolicy
from fireREST.fmc.policy.filepolicy import FilePolicy
from fireREST.fmc.policy.flexconfigpolicy import FlexConfigPolicy
from fireREST.fmc.policy.ftdnatpolicy import FtdNatPolicy
from fireREST.fmc.policy.ftdplatformsettingspolicy import FtdPlatformSettingsPolicy
from fireREST.fmc.policy.ftds2svpn import FtdS2sVpn
from fireREST.fmc.policy.healthpolicy import HealthPolicy
from fireREST.fmc.policy.identitypolicy import IdentityPolicy
from fireREST.fmc.policy.intrusionpolicy import IntrusionPolicy
from fireREST.fmc.policy.networkanalysispolicy import NetworkAnalysisPolicy
from fireREST.fmc.policy.policylock import PolicyLock
from fireREST.fmc.policy.prefilterpolicy import PrefilterPolicy
from fireREST.fmc.policy.ravpn import RaVpn
from fireREST.fmc.policy.snmpalert import SnmpAlert
from fireREST.fmc.policy.syslogalert import SyslogAlert
from fireREST.fmc.policy.umbrelladnspolicy import UmbrellaDnsPolicy


class Policy:
    def __init__(self, conn: Connection):
        self.accesspolicy = AccessPolicy(conn)
        self.dnspolicy = DnsPolicy(conn)
        self.dynamicaccesspolicy = DynamicAccessPolicy(conn)
        self.filepolicy = FilePolicy(conn)
        self.flexconfigpolicy = FlexConfigPolicy(conn)
        self.ftdnatpolicy = FtdNatPolicy(conn)
        self.ftdplatformsettingspolicy = FtdPlatformSettingsPolicy(conn)
        self.ftds2svpn = FtdS2sVpn(conn)
        self.healthpolicy = HealthPolicy(conn)
        self.identitypolicy = IdentityPolicy(conn)
        self.intrusionpolicy = IntrusionPolicy(conn)
        self.networkanalysispolicy = NetworkAnalysisPolicy(conn)
        self.policylock = PolicyLock(conn)
        self.prefilterpolicy = PrefilterPolicy(conn)
        self.ravpn = RaVpn(conn)
        self.snmpalert = SnmpAlert(conn)
        self.syslogalert = SyslogAlert(conn)
        self.umbrelladnspolicy = UmbrellaDnsPolicy(conn)
