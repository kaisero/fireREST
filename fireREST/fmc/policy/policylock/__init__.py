from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class PolicyLock(Resource):
    PATH = '/policy/policylocks/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
