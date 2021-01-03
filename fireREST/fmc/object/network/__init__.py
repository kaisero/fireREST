from fireREST import utils
from fireREST.fmc import Connection, Resource


class Network(Resource):
    PATH = '/object/networks/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.1.0'
    SUPPORTED_FILTERS = ['name_or_value', 'unused_only']
    SUPPORTED_PARAMS = ['override_target_id']

    @utils.support_params
    def get(self, uuid=None, name=None, name_or_value=None, unused_only=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
