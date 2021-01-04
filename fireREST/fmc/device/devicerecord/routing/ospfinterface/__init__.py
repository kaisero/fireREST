from fireREST.fmc import ChildResource


class OspfInterface(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ospfinterface/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
