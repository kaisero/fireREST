from fireREST.fmc import Resource


class AnyProtocolPortObject(Resource):
    PATH = '/object/anyprotocolportobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
