from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class InternalCertGroup(Resource):
    PATH = '/object/internalcertgroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
