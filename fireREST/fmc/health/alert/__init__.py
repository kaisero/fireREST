from fireREST import utils
from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class Alert(Resource):
    PATH = '/health/alerts/{uuid}'
    SUPPORTED_FILTERS = ['start_time', 'end_time', 'device_uuids', 'status', 'module_ids']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670

    @utils.support_params
    def get(self, start_time=None, end_time=None, device_uuids=None, status=None, module_ids=None, params=None):
        return super().get(params=params)
