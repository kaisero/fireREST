from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class SiDnsList(Resource):
    PATH = '/object/sidnslists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
