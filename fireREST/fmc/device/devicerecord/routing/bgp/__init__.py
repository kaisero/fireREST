from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource


class Bgp(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/bgp/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
