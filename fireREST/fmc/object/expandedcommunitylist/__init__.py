from fireREST.fmc import Resource


class ExpandedCommunityList(Resource):
    PATH = '/object/expandedcommunitylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
