from fireREST.fmc import Resource


class IseSecurityGroupTag(Resource):
    PATH = '/object/isesecuritygrouptags/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
