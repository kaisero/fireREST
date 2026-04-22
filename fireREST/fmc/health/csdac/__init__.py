from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class Csdac(Resource):
    PATH = '/health/csdac/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
