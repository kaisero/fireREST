from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class IntrusionRuleGroup(ChildResource):
    """Retrieves the per-policy behaviour of the specified intrusion rule ID for the target intrusion policy ID.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllSnort3IntrusionRuleGroups` (GET (list))
    - `getSnort3IntrusionRuleGroups` (GET)
    - `updateMultipleSnort3IntrusionRuleGroups` (UPDATE (bulk))
    - `updateSnort3IntrusionRuleGroups` (UPDATE)

    **Query parameters:**

    - `removeRuleOverrides` (boolean, optional): Boolean value for removing the rule overrides when excluding a rulegroup from a policy.
    - `includeCount` (boolean, optional): Boolean value if the count of rules should be calculated in the response.
    - `filter` (string, optional): Value can be any of the formats (including quotes): `"name:Browser/Firefox"` or `"currentSecurityLevel:DISABLED"` or `"showonlyparents:{true/false}"` or `"isSystemDefined:{true/false}"` or `"includeCount:true"`.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): [DEV ERROR: Missing description]
    """
    CONTAINER_NAME = 'IntrusionPolicy'
    CONTAINER_PATH = '/policy/intrusionpolicies/{uuid}'
    PATH = '/policy/intrusionpolicies/{container_uuid}/intrusionrulegroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
