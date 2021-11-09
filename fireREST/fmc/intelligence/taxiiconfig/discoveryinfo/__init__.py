from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import Resource


class DiscoveryInfo(Resource):
    NAMESPACE = 'tid'
    PATH = '/taxiiconfig/discoveryinfo/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
