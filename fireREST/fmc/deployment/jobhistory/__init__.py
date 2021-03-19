from fireREST.fmc import Resource


class JobHistory(Resource):
    PATH = '/deployment/jobhistories/{uuid}'
    SUPPORTED_FILTERS = ['device_uuid']
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.7.0'
