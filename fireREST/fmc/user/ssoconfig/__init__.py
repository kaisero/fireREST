from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class SsoConfig(Resource):
    PATH = '/users/ssoconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_670
