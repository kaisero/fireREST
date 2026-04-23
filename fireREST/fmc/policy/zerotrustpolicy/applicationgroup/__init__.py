from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ApplicationGroup(ChildResource):
    CONTAINER_NAME = 'ZeroTrustPolicy'
    CONTAINER_PATH = '/policy/zerotrustpolicies/{uuid}'
    PATH = '/policy/zerotrustpolicies/{container_uuid}/applicationgroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
