from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.ftds2svpn.advancedsettings import AdvancedSettings
from fireREST.fmc.policy.ftds2svpn.endpoint import Endpoint
from fireREST.fmc.policy.ftds2svpn.ikesettings import IkeSettings
from fireREST.fmc.policy.ftds2svpn.ipseccryptomap import IpsecCryptoMap
from fireREST.fmc.policy.ftds2svpn.ipsecsettings import IpsecSettings
from fireREST.fmc.policy.ftds2svpn.s2svpnsummary import S2sVpnSummary


class FtdS2sVpn(Resource):
    """Retrieves the Firewall Threat Defense Site to Site VPN topology associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDS2SVpnModel` (GET (list))
    - `getFTDS2SVpnModel` (GET)
    - `createFTDS2SVpnModel` (CREATE)
    - `updateFTDS2SVpnModel` (UPDATE)
    - `deleteFTDS2SVpnModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
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
        self.ipseccryptomap = IpsecCryptoMap(conn)
        self.ipsecsettings = IpsecSettings(conn)
        self.s2svpnsummary = S2sVpnSummary(conn)
