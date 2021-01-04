from fireREST.fmc import Resource


class Collection(Resource):
    NAMESPACE = 'tid'
    PATH = '/taxiiconfig/collections/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.2.3'
