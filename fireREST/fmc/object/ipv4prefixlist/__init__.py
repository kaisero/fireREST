from fireREST.fmc import Resource


class Ipv4PrefixList(Resource):
    PATH = '/object/ipv4prefixlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
