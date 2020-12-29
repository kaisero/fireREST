from fireREST.defaults import API_CONFIG_NAME
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.prefilterpolicy.prefilterrule import PrefilterRule
from fireREST.fmc.policy.prefilterpolicy.defaultaction import DefaultAction
from fireREST.fmc.policy.prefilterpolicy.operational import Operational


class PrefilterPolicy(Resource):
    PATH = '/policy/prefilterpolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = '6.5.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.5.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.5.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.5.0'

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.accessrule = PrefilterRule(conn)
        self.defaultaction = DefaultAction(conn)
        self.operational = Operational(conn)
