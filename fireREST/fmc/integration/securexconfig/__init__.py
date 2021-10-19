from fireREST.fmc import Resource


class SecurexConfig(Resource):
    PATH = '/integration/securexconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
