from fireREST.fmc import Resource


class ApplicationCategory(Resource):
    PATH = '/object/applicationcategories/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
