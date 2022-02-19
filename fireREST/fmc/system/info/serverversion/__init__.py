from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class ServerVersion(Resource):
    NAMESPACE = 'platform'
    PATH = '/info/serverversion/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
