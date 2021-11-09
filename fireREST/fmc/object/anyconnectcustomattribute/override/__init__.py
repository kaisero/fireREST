from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'AnyconnectCustomAttribute'
    CONTAINER_PATH = '/object/anyconnectcustomattributes/{uuid}'
    PATH = '/object/anyconnectcustomattributes/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
