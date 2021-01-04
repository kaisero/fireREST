from fireREST.fmc import Resource


class CloudRegion(Resource):
    PATH = '/integration/cloudregions/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.5.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.5.0'
