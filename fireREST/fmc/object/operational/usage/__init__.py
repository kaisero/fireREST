from fireREST import utils
from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class Usage(Resource):
    PATH = '/objects/operational/usage'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    SUPPORTED_FILTERS = ['uuid', 'obj_type']

    @utils.support_params
    def get(self, uuid: str, obj_type: str, params=None):
        return super().get(params=params)
