from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class Metric(Resource):
    PATH = '/health/metrics/{uuid}'
    SUPPORTED_FILTERS = ['metric', 'start_time', 'end_time', 'device_uuids', 'step', 'regex_filter', 'query_function']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
