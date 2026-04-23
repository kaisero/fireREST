from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class FileType(Resource):
    PATH = '/object/filetypes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
