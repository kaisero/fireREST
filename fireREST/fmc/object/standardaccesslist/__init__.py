from fireREST.fmc import Resource


class StandardAccessList(Resource):
    PATH = '/object/standardaccesslists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
