from fireREST import utils
from fireREST.defaults import API_RELEASE_610, API_RELEASE_740
from fireREST.exceptions import UnsupportedOperationError
from fireREST.fmc import Resource


class TaskStatus(Resource):
    PATH = '/job/taskstatuses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610

    def get(self, uuid=None, name=None, params=None):
        if not uuid:
            raise UnsupportedOperationError(msg='TaskStatus only supports GETBYID operations. UUID must be specified.')
        return super().get(uuid, params=params)

    @utils.minimum_version_required(version=API_RELEASE_740)
    def download_reports(self, uuid: str, params=None):
        url = self.url(f'/job/taskstatuses/{uuid}/operational/downloadreports')
        return self.conn.get(url=url, params=params)
