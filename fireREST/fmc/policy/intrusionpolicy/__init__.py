from fireREST.defaults import API_RELEASE_610, API_RELEASE_670
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.intrusionpolicy.intrusionrule import IntrusionRule
from fireREST.fmc.policy.intrusionpolicy.intrusionrulegroup import IntrusionRuleGroup


class IntrusionPolicy(Resource):
    """Retrieves the intrusion policy associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIntrusionPolicy` (GET (list))
    - `getIntrusionPolicy` (GET)
    - `createIntrusionPolicy` (CREATE)
    - `updateIntrusionPolicy` (UPDATE)
    - `deleteIntrusionPolicy` (DELETE)

    **Query parameters:**

    - `includeCount` (boolean, optional): Boolean value if the count of rules should be calculated in the response.
    - `ruleFilter` (string, optional): Query Param to return rule counts based on the filter. Value is of format `fts:browser`.
    - `replicateInspectionMode` (string, optional): Flag to replicate inspection mode from Snort 3 version to Snort 2 version.
    - `ruleRecommendationAction` (string, optional): This is a query parameter. Based on this value, the rule recommendation configuration is set against Snort3 Intrusion Policy. GENERATE - Generates the rule recommendation for the given recommendedSecurityLevel value and network objects per Snort3 Intrusion Policy. GENERATEANDACCEPT - Generates the rule recommendation for the given recommendedSecurityLevel value and network objects per Snort3 Intrusion Policy and accepts it against the Snort3 Intrusion Policy. REFRESH - Refreshes the rule recommendation for already given recommendedSecurityLevel value and network objects per Snort3 Intrusion Policy. REMOVE - Removes all rule recommendations and ruleRecommendation config per Snort3 Intrusion Policy. ACCEPT - Accepts the rule recommendation for which rule recommendation is already generated for the given recommendedSecurityLevel value and network objects against the given Snort3 Intrusion Policy
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/intrusionpolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_670

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.intrusionrule = IntrusionRule(conn)
        self.intrusionrulegroup = IntrusionRuleGroup(conn)
