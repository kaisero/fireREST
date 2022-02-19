from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import Resource


class StandardCommunityList(Resource):
    PATH = '/object/standardcommunitylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
