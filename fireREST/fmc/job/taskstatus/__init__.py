from fireREST import utils
from fireREST.defaults import API_RELEASE_610, API_RELEASE_740
from fireREST.exceptions import UnsupportedOperationError
from fireREST.fmc import Resource


class TaskStatus(Resource):
    """Retrieves information about a previously submitted pending job/task with the specified ID.

    **Tags:** Status

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllTaskStatus` (GET (list))
    - `getTaskStatus` (GET)

    **Query parameters:**

    - `showDetailedDeviceStatus` (boolean, optional): Query parameter to show the detailed status of devices for type : DEVICEDEPLOYMENT and DEVICEROLLBACK
    - `filter` (string): Filter criteria can be specified using the format `type:{type};status:{status};`. `type` -- Type of task to be returned. It is mandatory field. Allowed values are `"{Deployment | Registration | Unregistration | PendingChangesRequest}"`. `status` -- Filter based on the status of the task. It is mandatory field. &emsp;Allowed values for `Deployment` task are `"{Deploying | Cancelled | Failed | Succeeded}"`. &emsp;Allowed values for `Registration` task are `"{Pending | Running | Success | Failed}"`. &emsp;Allowed values for `Unregistration` task are `"{Running | Success | Failed}"`. &emsp;Allowed values for `PendingChangesRequest` task are `"{Running | Success | Failed}"`.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

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
