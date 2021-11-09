from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class Application(Resource):
    PATH = '/object/applications/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
