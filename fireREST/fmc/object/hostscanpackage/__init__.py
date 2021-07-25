from fireREST.fmc import Resource


class HostscanPackage(Resource):
    PATH = '/object/hostscanpackages/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
