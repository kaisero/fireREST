from fireREST.fmc import Resource


class Domain(Resource):
    NAMESPACE = 'platform'
    PATH = '/info/domain/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
