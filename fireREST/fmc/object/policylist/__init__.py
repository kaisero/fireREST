from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import Resource


class PolicyList(Resource):
    PATH = '/object/policylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
