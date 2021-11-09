from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import ChildResource


class IkeSettings(ChildResource):
    CONTAINER_NAME = 'FtdS2sVpn'
    CONTAINER_PATH = '/policy/ftds2svpns/{uuid}'
    PATH = '/policy/ftds2svpns/{container_uuid}/ikesettings/{uuid}'
    SUPPORTED_FILTERS = []
    SUPPORTED_PARAMS = []
    IGNORE_FOR_CREATE = []
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
