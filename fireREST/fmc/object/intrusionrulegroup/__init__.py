from fireREST import utils
from fireREST.fmc import Resource


class IntrusionRuleGroup(Resource):
    PATH = '/object/intrusionrulegroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '7.0.0'

    SUPPORTED_FILTERS = ['name', 'current_security_level', 'show_only_parents', 'include_count']

    @utils.support_params
    def get(
        self, uuid=None, name=None, current_security_level=None, show_only_parents=None, include_count=None, params=None
    ):
        return super().get(uuid=uuid, name=name, params=params)
