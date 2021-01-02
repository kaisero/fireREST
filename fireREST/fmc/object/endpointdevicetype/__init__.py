from fireREST.fmc import Resource


class EndpointDeviceType(Resource):
    PATH = '/object/endpointdevicetypes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
