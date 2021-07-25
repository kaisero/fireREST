from fireREST.fmc import Resource


class SiDnsFeed(Resource):
    PATH = '/object/sidnsfeeds/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
