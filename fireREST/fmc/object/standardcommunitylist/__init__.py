from fireREST.fmc import Resource


class StandardCommunityList(Resource):
    PATH = '/object/standardcommunitylists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
