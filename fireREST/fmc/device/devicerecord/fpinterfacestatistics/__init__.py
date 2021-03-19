from fireREST.fmc import ChildResource


class FpInterfaceStatistics(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/fpinterfacestatistics/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
