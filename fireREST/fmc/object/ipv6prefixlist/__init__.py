from fireREST.fmc import Resource


class Ipv6PrefixList(Resource):
    PATH = '/object/ipv6prefixlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
