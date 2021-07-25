from fireREST.fmc import Resource


class CertificateMap(Resource):
    PATH = '/object/certificatemaps/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
