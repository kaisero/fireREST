from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import Resource


class CertEnrollment(Resource):
    PATH = '/object/certenrollments/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
