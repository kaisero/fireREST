from fireREST.fmc import ChildResource


class ApplicableDevice(ChildResource):
    CONTAINER_NAME = 'UpgradePackage'
    CONTAINER_PATH = '/updates/upgradepackages/{uuid}'
    NAMESPACE = 'platform'
    PATH = '/updates/upgradepackages/{container_uuid}/applicabledevices/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.3.0'
