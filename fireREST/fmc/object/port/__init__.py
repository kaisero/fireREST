from fireREST.fmc import Resource


class Port(Resource):
    PATH = '/object/ports/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
