from fireREST.fmc import Resource


class CertEnrollment(Resource):
    PATH = '/object/certenrollments/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.4.0'
