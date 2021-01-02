from fireREST.fmc import Resource


class ExtendedAccessList(Resource):
    PATH = '/object/extendedaccesslists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.3.0'
