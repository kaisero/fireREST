from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.ftdplatformsettingspolicy.httpaccesssettings import HttpAccessSettings
from fireREST.fmc.policy.ftdplatformsettingspolicy.netflowpolicies import NetflowPolicies
from fireREST.fmc.policy.ftdplatformsettingspolicy.snmpsettings import SnmpSettings


class FtdPlatformSettingsPolicy(Resource):
    """Retrieves the FTDPlatformSettings Policy with the associated ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDPlatformSettingsPolicy` (GET (list))
    - `getFTDPlatformSettingsPolicy` (GET)
    - `createFTDPlatformSettingsPolicy` (CREATE)
    - `updateFTDPlatformSettingsPolicy` (UPDATE)
    - `deleteFTDPlatformSettingsPolicy` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:policyname` `policyname` -- Name of the FTDPlatformSettings Policy to be queried.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/ftdplatformsettingspolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.httpaccesssettings = HttpAccessSettings(conn)
        self.netflowpolicies = NetflowPolicies(conn)
        self.snmpsettings = SnmpSettings(conn)
