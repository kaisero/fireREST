from fireREST.fmc import Resource


class KeyChain(Resource):
    PATH = '/object/keychains/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.4.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.4.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.4.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.4.0'

