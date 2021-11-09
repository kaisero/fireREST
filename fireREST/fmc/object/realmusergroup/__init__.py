from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class RealmUserGroup(Resource):
    PATH = '/object/realmusergroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
