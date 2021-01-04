from fireREST.fmc import Resource


class TaskStatus(Resource):
    PATH = '/job/taskstatus/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
