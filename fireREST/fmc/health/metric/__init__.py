from fireREST import utils
from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class Metric(Resource):
    PATH = '/health/metrics/{uuid}'
    SUPPORTED_FILTERS = ['device_uuids', 'end_time', 'metric', 'regex_filter', 'query_function', 'start_time', 'step']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670

    @utils.support_params
    def get(
        self,
        device_uuids=None,
        end_time=None,
        metric=None,
        regex_filter=None,
        query_function=None,
        start_time=None,
        step=None,
        params=None,
    ):
        return super().get(params=params)
