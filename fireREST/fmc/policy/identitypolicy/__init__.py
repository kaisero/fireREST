from fireREST.fmc import Resource


class IdentityPolicy(Resource):
    PATH = '/policy/identitypolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
