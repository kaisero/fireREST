from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import Resource


class ExpandedCommunityList(Resource):
    PATH = '/object/expandedcommunitylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
