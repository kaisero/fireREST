from fireREST import utils
from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import ChildResource


class Hitcount(ChildResource):
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/operational/hitcounts/{uuid}'
    SUPPORTED_FILTERS = ['device_id', 'ids', 'fetch_zero_hitcount']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_640

    @utils.support_params
    def update(self):
        return

    @utils.support_params
    def get(self, container_uuid, device_id=None, ids=None, fetch_zero_hitcount=None, params=None):
        return super().get(container_uuid, params=params)

    @utils.support_params
    def delete(self):
        return
