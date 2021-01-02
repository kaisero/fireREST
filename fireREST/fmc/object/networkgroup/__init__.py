from fireREST.fmc import Resource


class NetworkGroup(Resource):
    PATH = '/object/networkgroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.1.0'

