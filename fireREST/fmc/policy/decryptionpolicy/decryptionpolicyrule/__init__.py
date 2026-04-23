from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class DecryptionPolicyRule(ChildResource):
    CONTAINER_NAME = 'DecryptionPolicy'
    CONTAINER_PATH = '/policy/decryptionpolicies/{uuid}'
    PATH = '/policy/decryptionpolicies/{container_uuid}/decryptionpolicyrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
