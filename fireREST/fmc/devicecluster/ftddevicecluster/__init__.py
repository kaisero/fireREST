from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import Resource


class FtdDeviceCluster(Resource):
    PATH = '/deviceclusters/ftddevicecluster/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
