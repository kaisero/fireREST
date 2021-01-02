from fireREST.fmc import Resource


class Continent(Resource):
    PATH = '/object/continent/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
