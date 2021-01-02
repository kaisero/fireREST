from fireREST.fmc import Resource


class GlobalTimeZone(Resource):
    PATH = '/object/globaltimezones/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
