from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.chassisplatformsettingspolicy.accesslistsettings import AccessListSettings
from fireREST.fmc.policy.chassisplatformsettingspolicy.dnssettings import DnsSettings
from fireREST.fmc.policy.chassisplatformsettingspolicy.sshclientsettings import SshClientSettings
from fireREST.fmc.policy.chassisplatformsettingspolicy.sshserversettings import SshServerSettings
from fireREST.fmc.policy.chassisplatformsettingspolicy.syslogsettings import SyslogSettings
from fireREST.fmc.policy.chassisplatformsettingspolicy.timesynchronizationsettings import TimeSynchronizationSettings
from fireREST.fmc.policy.chassisplatformsettingspolicy.timezonesettings import TimezoneSettings


class ChassisPlatformSettingsPolicy(Resource):
    """Retrieves the chassis platform settings policies associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllChassisPlatformSettingsPolicy` (GET (list))
    - `getChassisPlatformSettingsPolicy` (GET)
    - `createChassisPlatformSettingsPolicy` (CREATE)
    - `updateChassisPlatformSettingsPolicy` (UPDATE)
    - `deleteChassisPlatformSettingsPolicy` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/chassisplatformsettingspolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.accesslistsettings = AccessListSettings(conn)
        self.dnssettings = DnsSettings(conn)
        self.sshclientsettings = SshClientSettings(conn)
        self.sshserversettings = SshServerSettings(conn)
        self.syslogsettings = SyslogSettings(conn)
        self.timesynchronizationsettings = TimeSynchronizationSettings(conn)
        self.timezonesettings = TimezoneSettings(conn)
