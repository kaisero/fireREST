from fireREST.fmc import Resource


class ApplicationRisk(Resource):
    PATH = '/object/applicationrisks/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
