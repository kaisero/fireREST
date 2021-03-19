from fireREST.fmc import Resource


class SiUrlFeed(Resource):
    PATH = '/object/siurlfeeds/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'
