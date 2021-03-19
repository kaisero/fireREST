from fireREST.fmc import Resource


class RealmUserGroup(Resource):
    PATH = '/object/realmusergroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
