from fireREST.fmc import Resource


class SiNetworkFeed(Resource):
    PATH = '/object/sinetworkfeeds/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
