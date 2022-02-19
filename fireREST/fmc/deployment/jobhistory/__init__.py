from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class JobHistory(Resource):
    PATH = '/deployment/jobhistories/{uuid}'
    SUPPORTED_FILTERS = ['device_uuid']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
