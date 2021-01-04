from fireREST.fmc import Resource


class CommunityList(Resource):
    PATH = '/object/communitylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.5.0'
