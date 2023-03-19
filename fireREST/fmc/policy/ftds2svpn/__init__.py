from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.ftds2svpn.advancedsettings import AdvancedSettings
from fireREST.fmc.policy.ftds2svpn.endpoint import Endpoint
from fireREST.fmc.policy.ftds2svpn.ikesettings import IkeSettings
from fireREST.fmc.policy.ftds2svpn.ipsecsettings import IpsecSettings


class FtdS2sVpn(Resource):
    PATH = '/policy/ftds2svpns/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.advancedsettings = AdvancedSettings(conn)
        self.endpoint = Endpoint(conn)
        self.ikesettings = IkeSettings(conn)
        self.ipsecsettings = IpsecSettings(conn)
