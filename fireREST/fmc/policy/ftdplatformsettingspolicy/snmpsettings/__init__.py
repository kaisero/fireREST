from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class SnmpSettings(ChildResource):
    CONTAINER_NAME = 'FtdPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/ftdplatformsettingspolicies/{uuid}'
    PATH = '/policy/ftdplatformsettingspolicies/{container_uuid}/snmpsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
