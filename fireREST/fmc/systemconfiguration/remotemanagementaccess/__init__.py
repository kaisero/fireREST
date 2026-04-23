from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class RemoteManagementAccess(Resource):
    NAMESPACE = 'platform'
    PATH = '/systemconfiguration/remotemanagementaccess/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
