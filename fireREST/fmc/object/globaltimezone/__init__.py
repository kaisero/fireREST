from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import Resource


class GlobalTimeZone(Resource):
    PATH = '/object/globaltimezones/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
