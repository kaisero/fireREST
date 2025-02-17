from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import Resource


class File(Resource):
    NAMESPACE = 'troubleshoot'
    PATH = '/packettracer/files/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
