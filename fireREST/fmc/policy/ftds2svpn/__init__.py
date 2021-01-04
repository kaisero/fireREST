from fireREST import utils
from fireREST.defaults import API_CONFIG_NAME
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.ftds2svpn.advancedsettings import AdvancedSettings
from fireREST.fmc.policy.ftds2svpn.endpoint import Endpoint
from fireREST.fmc.policy.ftds2svpn.ikesettings import IkeSettings
from fireREST.fmc.policy.ftds2svpn.ipsecsettings import IpsecSettings


class FtdS2sVpn(Resource):
    PATH = '/policy/ftds2svpns/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_CREATE = '6.3.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.3.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.3.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.3.0'

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.advancedsettings = AdvancedSettings(conn)
        self.endpoint = Endpoint(conn)
        self.ikesettings = IkeSettings(conn)
        self.ipsecsettings = IpsecSettings(conn)
