from fireREST.fmc import Resource


class Realm(Resource):
    PATH = '/object/realms/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '7.0.0'
