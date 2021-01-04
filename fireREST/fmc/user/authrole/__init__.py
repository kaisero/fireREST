from fireREST.fmc import Resource


class AuthRole(Resource):
    PATH = '/users/authroles/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.7.0'
