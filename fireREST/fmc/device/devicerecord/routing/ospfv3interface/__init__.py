from fireREST.fmc import ChildResource


class Ospfv3Interface(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ospfv3interfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
