from fireREST.fmc import Resource


class SiDnsList(Resource):
    PATH = '/object/sidnslists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
