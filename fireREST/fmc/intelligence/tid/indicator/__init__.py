from fireREST.fmc import Resource


class Indicator(Resource):
    NAMESPACE = 'tid'
    PATH = '/tid/indicator/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.2.3'
