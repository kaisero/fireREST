from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'SsoServer'
    CONTAINER_PATH = '/object/ssoservers/{uuid}'
    PATH = '/object/ssoservers/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
