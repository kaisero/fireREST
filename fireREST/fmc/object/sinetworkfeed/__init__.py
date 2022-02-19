from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class SiNetworkFeed(Resource):
    PATH = '/object/sinetworkfeeds/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
