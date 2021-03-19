from fireREST.fmc import Resource


class RollbackRequest(Resource):
    PATH = '/deployment/rollbackrequests/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_CREATE = '6.7.0'
