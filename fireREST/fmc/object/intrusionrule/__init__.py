from fireREST import utils
from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class IntrusionRule(Resource):
    PATH = '/object/intrusionrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700

    SUPPORTED_FILTERS = ['gid', 'sid', 'overrides', 'ips_policy', 'fts']

    @utils.support_params
    def get(self, uuid=None, name=None, gid=None, sid=None, overrides=None, ips_policy=None, fts=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
