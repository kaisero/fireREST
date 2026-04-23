from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class PendingChangesRequest(Resource):
    PATH = '/deployment/pendingchangesrequests/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
