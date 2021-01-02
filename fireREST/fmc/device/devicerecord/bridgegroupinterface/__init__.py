from fireREST.fmc import ChildResource


class BridgeGroupInterface(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/bridgegroupinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.1.0'
