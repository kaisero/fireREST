from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class AuthRole(Resource):
    PATH = '/users/authroles/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
