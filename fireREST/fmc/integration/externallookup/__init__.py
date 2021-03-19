from fireREST.fmc import Resource


class ExternalLookup(Resource):
    PATH = '/integration/externallookups/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_CREATE = '6.4.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.4.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.4.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.4.0'
