from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ActiveSessions(Resource):
    PATH = '/analysis/activesessions/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
