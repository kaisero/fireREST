from fireREST.fmc import ChildResource


class VirtualRouter(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.6.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.6.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.6.0'
