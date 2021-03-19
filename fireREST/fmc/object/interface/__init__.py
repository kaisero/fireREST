from fireREST.fmc import Resource


class Interface(Resource):
    PATH = '/object/interfaceobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.3.0'
