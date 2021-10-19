from fireREST import utils
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.host.override import Override


class IntrusionRule(Resource):
    PATH = '/object/intrusionrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '7.0.0'

    SUPPORTED_FILTERS = ['gid', 'sid', 'overrides', 'ips_policy', 'fts']

    @utils.support_params
    def get(self, uuid=None, name=None, gid=None, sid=None, overrides=None, ips_policy=None, fts=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
