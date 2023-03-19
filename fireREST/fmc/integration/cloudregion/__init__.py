from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import Resource


class CloudRegion(Resource):
    PATH = '/integration/cloudregions/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_650
