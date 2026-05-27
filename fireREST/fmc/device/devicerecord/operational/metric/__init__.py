from fireREST import utils
from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource


class Metric(ChildResource):
    """Retrieves HealthMonitor metrics for the device.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getHealthMonitorModel` (GET (list))

    **Query parameters:**

    - `filter` (string): The metric filter query parameter should have healthmonitor name.Currently supports only `metric:memory & metric:cpu`
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/operational/metrics'
    SUPPORTED_FILTERS = ['metric']

    @utils.support_params
    @utils.resolve_by_name
    @utils.minimum_version_required(version=API_RELEASE_660)
    def get(self, metric: str, container_uuid=None, container_name=None, params=None):
        url = self.url(self.PATH.format(container_uuid=container_uuid))
        return self.conn.get(url=url, params=params)
