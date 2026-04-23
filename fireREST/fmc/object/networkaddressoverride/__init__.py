from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class NetworkAddressOverride(Resource):
    PATH = '/object/networkaddressoverrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
