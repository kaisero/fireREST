from fireREST.fmc import Resource


class ApplicationProductivity(Resource):
    PATH = '/object/applicationproductivities/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
