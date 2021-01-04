from fireREST.fmc import Resource


class VariableSet(Resource):
    PATH = '/object/variablesets/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
