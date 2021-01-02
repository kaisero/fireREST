from fireREST.fmc import Resource


class Element(Resource):
    NAMESPACE = 'tid'
    PATH = '/tid/element/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'
