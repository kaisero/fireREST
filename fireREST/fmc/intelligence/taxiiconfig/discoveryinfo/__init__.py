from fireREST.fmc import Resource


class DiscoveryInfo(Resource):
    NAMESPACE = 'tid'
    PATH = '/taxiiconfig/discoveryinfo/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.2.3'
