from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class VirtualAccessInterface(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/operational/virtualaccessinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
