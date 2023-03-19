from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import Resource


class DuoConfig(Resource):
    PATH = '/users/duoconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
