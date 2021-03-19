from fireREST.fmc import Resource


class ExternalStorage(Resource):
    PATH = '/integration/externalstorage/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_CREATE = '6.7.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.7.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.7.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.7.0'
