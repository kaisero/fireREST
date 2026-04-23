from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class DistinguishedName(Resource):
    PATH = '/object/distinguishednames/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
