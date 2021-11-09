from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import Resource


class Element(Resource):
    NAMESPACE = 'tid'
    PATH = '/tid/element/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
