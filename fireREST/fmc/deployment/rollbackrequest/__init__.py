from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class RollbackRequest(Resource):
    PATH = '/deployment/rollbackrequests/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_670
