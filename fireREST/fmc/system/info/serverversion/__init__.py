from fireREST.fmc import Resource


class ServerVersion(Resource):
    NAMESPACE = 'platform'
    PATH = '/info/serverversion/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
