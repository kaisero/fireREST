from fireREST.fmc import Resource


class NetworkAddress(Resource):
    PATH = '/object/networkaddresses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
