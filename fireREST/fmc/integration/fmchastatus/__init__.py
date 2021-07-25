from fireREST.fmc import Resource


class FmcHaStatus(Resource):
    PATH = '/integration/fmchastatuses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
