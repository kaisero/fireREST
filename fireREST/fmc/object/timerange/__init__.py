from fireREST.fmc import Resource


class Timerange(Resource):
    PATH = '/object/timeranges/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.6.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.6.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.6.0'
