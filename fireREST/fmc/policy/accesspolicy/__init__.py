from fireREST import utils
from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.accesspolicy.accessrule import AccessRule
from fireREST.fmc.policy.accesspolicy.category import Category
from fireREST.fmc.policy.accesspolicy.defaultaction import DefaultAction
from fireREST.fmc.policy.accesspolicy.inheritancesettings import InheritanceSettings
from fireREST.fmc.policy.accesspolicy.loggingsettings import LoggingSettings
from fireREST.fmc.policy.accesspolicy.operational import Operational
from fireREST.fmc.policy.accesspolicy.securityintelligencepolicy import SecurityIntelligencePolicy


class AccessPolicy(Resource):
    """Retrieves the access control policy associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllAccessPolicy` (GET (list))
    - `getAccessPolicy` (GET)
    - `createAccessPolicy` (CREATE)
    - `updateAccessPolicy` (UPDATE)
    - `deleteAccessPolicy` (DELETE)

    **Query parameters:**

    - `ignoreWarning` (boolean, optional): Shows any warnings when deleting an access policy, if set to false. If not specified, value is set to true and warnings are ignored. Allowed values are true and false.
    - `name` (string, optional): If parameter is specified, only the policy matching with the specified name will be displayed.
    - `filter` (string, optional): Value is of format (including quotes): `"locked:{true|false}"` `locked`query parameter when set to 'true' returns list of Access Policies which are locked and when set to 'false' returns policies which are unlocked.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/accesspolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
    SUPPORTED_PARAMS = ['name']

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.accessrule = AccessRule(conn)
        self.category = Category(conn)
        self.defaultaction = DefaultAction(conn)
        self.inheritancesettings = InheritanceSettings(conn)
        self.loggingsettings = LoggingSettings(conn)
        self.operational = Operational(conn)
        self.securityintelligencepolicy = SecurityIntelligencePolicy(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
