from fireREST import utils
from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import Resource


class TunnelStatus(Resource):
    PATH = '/health/tunnelstatuses/{uuid}'
    SUPPORTED_FILTERS = ['device_id', 'deployed_status', 'sort_by', 'status', 'vpn_topology_id']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710

    @utils.support_params
    def get(self, device_id=None, deployed_status=None, sort_by=None, status=None, vpn_topology_id=None, params=None):
        return super().get(params=params)
