from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import ChildResource


class DefaultAction(ChildResource):
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/prefilterpolicies/{uuid}'
    PATH = '/policy/prefilterpolicies/{container_uuid}/defaultactions/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_650
