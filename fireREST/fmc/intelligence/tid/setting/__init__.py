from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import Resource


class Setting(Resource):
    NAMESPACE = 'tid'
    PATH = '/tid/settings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
