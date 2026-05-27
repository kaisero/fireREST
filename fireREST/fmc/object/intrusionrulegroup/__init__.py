from fireREST import utils
from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class IntrusionRuleGroup(Resource):
    """Retrieves, deletes, creates, or modifies Snort 3 intrusion rulegroup associated with the specified ID. If no ID is specified for a GET, retrieves list of all Snort 3 intrusion group objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSnort3IntrusionRuleGroupsObject` (GET (list))
    - `getSnort3IntrusionRuleGroupsObject` (GET)
    - `createMultipleSnort3IntrusionRuleGroupsObject` (CREATE)
    - `updateSnort3IntrusionRuleGroupsObject` (UPDATE)
    - `deleteSnort3IntrusionRuleGroupsObject` (DELETE)

    **Query parameters:**

    - `cascadeDeleteOrphanedRules` (boolean, optional): Boolean value for deleting orphan rule. Mandatory if custom rulegroup has unique/unshared rules which becomes orphan after custom rule Group delete.
    - `filter` (string, optional): Value can be any of the formats (including quotes): `"name:Browser/Firefox"` or `"currentSecurityLevel:DISABLED"` or `"showonlyparents:{true/false}"` or `"isSystemDefined:{true/false}"` or `"includeCount:true"`.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk Snort 3 rulegroup operations.
    """

    PATH = '/object/intrusionrulegroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700

    SUPPORTED_FILTERS = ['name', 'current_security_level', 'show_only_parents', 'include_count']

    @utils.support_params
    def get(
        self, uuid=None, name=None, current_security_level=None, show_only_parents=None, include_count=None, params=None
    ):
        return super().get(uuid=uuid, name=name, params=params)
