from fireREST.fmc import Resource


class ApplicationTag(Resource):
    PATH = '/object/applicationtags/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
