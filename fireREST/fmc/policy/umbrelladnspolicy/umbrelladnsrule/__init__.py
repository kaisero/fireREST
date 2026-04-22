from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class UmbrellaDnsRule(ChildResource):
    CONTAINER_NAME = 'UmbrellaDnsPolicy'
    CONTAINER_PATH = '/policy/umbrelladnspolicies/{uuid}'
    PATH = '/policy/umbrelladnspolicies/{container_uuid}/umbrelladnsrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
