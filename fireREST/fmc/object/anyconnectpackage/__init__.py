from fireREST import utils
from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource, Connection


class AnyconnectPackage(Resource):
    PATH = '/object/anyconnectpackages/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700

    SUPPORTED_FILTERS = ['name_or_value', 'unused_only']

    def __init__(self, conn: Connection):
        super().__init__(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, name_or_value=None, unused_only=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
