from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class SecurexConfig(Resource):
    PATH = '/integration/securexconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
