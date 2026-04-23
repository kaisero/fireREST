from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class NetflowPolicies(ChildResource):
    CONTAINER_NAME = 'FtdPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/ftdplatformsettingspolicies/{uuid}'
    PATH = '/policy/ftdplatformsettingspolicies/{container_uuid}/netflowpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
