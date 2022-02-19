from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import Resource


class AsPathList(Resource):
    PATH = '/object/aspathlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
