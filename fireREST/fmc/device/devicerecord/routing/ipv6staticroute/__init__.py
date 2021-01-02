from fireREST.fmc import ChildResource


class Ipv6StaticRoute(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ipv6staticroutes/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.2.3'
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.2.3'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.2.3'
