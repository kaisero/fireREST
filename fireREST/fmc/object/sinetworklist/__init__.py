from fireREST.fmc import Resource


class SiNetworkList(Resource):
    PATH = '/object/sinetworklists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
