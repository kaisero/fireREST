from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ExternalCertificate(Resource):
    PATH = '/object/externalcertificates/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
