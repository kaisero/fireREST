from fireREST.fmc import Resource


class Setting(Resource):
    NAMESPACE = 'tid'
    PATH = '/tid/settings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.2.3'
