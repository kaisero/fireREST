from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource


class ExtendedAccessList(Resource):
    PATH = '/object/extendedaccesslists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
