from fireREST.fmc import Resource


class GroupPolicy(Resource):
    PATH = '/object/grouppolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
