from fireREST.fmc import Resource


class SlaMonitor(Resource):
    PATH = '/object/slamonitors/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.2.3'
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.2.3'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.2.3'
