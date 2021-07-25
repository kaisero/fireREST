from fireREST.fmc import Resource


class Sinkhole(Resource):
    PATH = '/object/sinkholes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
