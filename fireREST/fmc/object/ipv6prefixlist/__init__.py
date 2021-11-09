from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import Resource


class Ipv6PrefixList(Resource):
    PATH = '/object/ipv6prefixlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
