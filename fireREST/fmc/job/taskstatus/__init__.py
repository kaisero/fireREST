from fireREST.exceptions import UnsupportedOperationError
from fireREST.fmc import Resource


class TaskStatus(Resource):
    PATH = '/job/taskstatuses/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'

    def get(self, uuid=None, name=None, params=None):
        if not uuid:
            raise UnsupportedOperationError(msg='TaskStatus only supports GETBYID operations. UUID must be specified.')
        return super().get(uuid, params=params)
