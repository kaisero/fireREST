from fireREST.fmc import Resource


class RealmUser(Resource):
    PATH = '/object/realmusers/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
