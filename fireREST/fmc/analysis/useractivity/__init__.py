from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class UserActivity(Resource):
    PATH = '/analysis/useractivity/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
