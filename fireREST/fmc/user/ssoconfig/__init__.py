from fireREST.fmc import Resource


class SsoConfig(Resource):
    PATH = '/users/ssoconfigs/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.7.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.7.0'
