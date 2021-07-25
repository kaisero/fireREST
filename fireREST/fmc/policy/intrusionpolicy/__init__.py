from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.intrusionpolicy.intrusionrule import IntrusionRule
from fireREST.fmc.policy.intrusionpolicy.intrusionrulegroup import IntrusionRuleGroup


class IntrusionPolicy(Resource):
    PATH = '/policy/intrusionpolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = '6.7.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.7.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.7.0'

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.intrusionrule = IntrusionRule(conn)
        self.intrusionrulegroup = IntrusionRuleGroup(conn)
