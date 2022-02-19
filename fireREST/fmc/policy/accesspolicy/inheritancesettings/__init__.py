from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import ChildResource


class InheritanceSettings(ChildResource):
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/inheritancesettings/{uuid}'
    SUPPORTED_FILTERS = []
    SUPPORTED_PARAMS = []
    IGNORE_FOR_CREATE = []
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_650
