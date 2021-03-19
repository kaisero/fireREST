from fireREST.fmc import Resource


class PolicyList(Resource):
    PATH = '/object/policylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.5.0'
