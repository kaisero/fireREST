from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.ftdplatformsettingspolicy.httpaccesssettings import HttpAccessSettings
from fireREST.fmc.policy.ftdplatformsettingspolicy.netflowpolicies import NetflowPolicies
from fireREST.fmc.policy.ftdplatformsettingspolicy.snmpsettings import SnmpSettings


class FtdPlatformSettingsPolicy(Resource):
    PATH = '/policy/ftdplatformsettingspolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.httpaccesssettings = HttpAccessSettings(conn)
        self.netflowpolicies = NetflowPolicies(conn)
        self.snmpsettings = SnmpSettings(conn)
