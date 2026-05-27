from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class EbsSnapshot(Resource):
    PATH = '/integration/ebssnapshots/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
