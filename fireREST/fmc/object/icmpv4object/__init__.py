from fireREST.fmc import Resource


class Icmpv4Object(Resource):
    PATH = '/object/icmpv4objects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.1.0'

