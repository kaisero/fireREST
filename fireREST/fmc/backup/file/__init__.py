from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class BackupFile(Resource):
    PATH = '/backup/files/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730
