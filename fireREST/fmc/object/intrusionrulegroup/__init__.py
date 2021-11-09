from fireREST import utils
from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class IntrusionRuleGroup(Resource):
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
