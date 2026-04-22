from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class PathMonitoredInterface(Resource):
    PATH = '/health/pathmonitoredinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
