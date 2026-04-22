from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class DownloadBackup(Resource):
    PATH = '/backup/downloadbackup/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
