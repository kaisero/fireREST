from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class Mapping(ChildResource):
    CONTAINER_NAME = 'DynamicObject'
    CONTAINER_PATH = '/object/dynamicobjects/{uuid}'
    PATH = '/object/dynamicobjects/{container_uuid}/mappings'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700
