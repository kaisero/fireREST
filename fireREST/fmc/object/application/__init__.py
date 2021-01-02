from fireREST.fmc import Resource


class Application(Resource):
    PATH = '/object/applications/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
