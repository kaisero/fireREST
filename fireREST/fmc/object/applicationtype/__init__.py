from fireREST.fmc import Resource


class ApplicationType(Resource):
    PATH = '/object/applicationtypes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
