from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class RealmUser(Resource):
    PATH = '/object/realmusers/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
