from fireREST.fmc import ChildResource


class FailoverInterfaceMacAddressConfig(ChildResource):
    CONTAINER_NAME = 'FtdDeviceHAPair'
    CONTAINER_PATH = '/devicehapairs/ftddevicehapairs/{uuid}'
    PATH = '/devicehapairs/ftddevicehapairs/{container_uuid}/failoverinterfacemacaddressconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.3.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.3.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.3.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.3.0'
