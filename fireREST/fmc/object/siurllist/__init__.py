from fireREST.fmc import Resource


class SiUrlList(Resource):
    PATH = '/object/siurllists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'
