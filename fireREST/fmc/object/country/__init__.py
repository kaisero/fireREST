from fireREST.fmc import Resource


class Country(Resource):
    PATH = '/object/countries/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
