from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import Resource


class Ipv4PrefixList(Resource):
    PATH = '/object/ipv4prefixlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
