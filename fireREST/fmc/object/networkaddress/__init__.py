from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class NetworkAddress(Resource):
    PATH = '/object/networkaddresses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
