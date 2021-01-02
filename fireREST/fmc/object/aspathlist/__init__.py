from fireREST.fmc import Resource


class AsPathList(Resource):
    PATH = '/object/aspathlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
