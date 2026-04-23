from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class TunnelDetails(ChildResource):
    CONTAINER_NAME = 'TunnelStatus'
    CONTAINER_PATH = '/health/tunnelstatuses/{uuid}'
    PATH = '/health/tunnelstatuses/{container_uuid}/tunneldetails/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
