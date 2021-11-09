from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class SiDnsFeed(Resource):
    PATH = '/object/sidnsfeeds/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
