from fireREST.fmc import Resource


class ApplicationFilter(Resource):
    PATH = '/object/applicationfilters/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
