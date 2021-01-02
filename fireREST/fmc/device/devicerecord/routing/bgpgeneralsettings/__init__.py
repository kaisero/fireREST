from fireREST.fmc import ChildResource


class BgpGeneralSettings(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/bgpgeneralsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
