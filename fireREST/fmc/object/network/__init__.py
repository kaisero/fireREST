from fireREST.defaults import API_CONFIG_NAME
from fireREST.fmc import Connection, Resource


class Network(Resource):
    PATH = '/object/networks/{uuid}'
    SUPPORTED_FILTERS = ['name_or_value', 'unused_only']
    SUPPORTED_OPERATIONS = ['create', 'get', 'update', 'delete']
    SUPPORTED_PARAMS = ['override_target_id']

    def get(self, uuid=None, name=None, name_or_value=None, unused_only=None, override_target_id=None, params=None):
        return super().get(self, uuid=uuid, name=name, params=params)
