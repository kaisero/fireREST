from fireREST.fmc import Resource


class FtdDeviceCluster(Resource):
    PATH = '/deviceclusters/ftddevicecluster/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.4.0'
