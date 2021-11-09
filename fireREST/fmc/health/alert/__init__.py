from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class Alert(Resource):
    PATH = '/health/alerts/{uuid}'
    SUPPORTED_FILTERS = ['start_time', 'end_time', 'device_uuids', 'status', 'module_ids']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
