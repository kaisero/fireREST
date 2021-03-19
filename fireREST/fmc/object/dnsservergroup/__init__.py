from fireREST.fmc import Resource


class DnsServerGroup(Resource):
    PATH = '/object/dnsservergroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.3.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.3.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.3.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.3.0'
