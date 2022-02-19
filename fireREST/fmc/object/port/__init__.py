from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class Port(Resource):
    PATH = '/object/ports/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
