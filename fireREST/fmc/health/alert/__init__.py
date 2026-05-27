from fireREST import utils
from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class Alert(Resource):
    """Retrieves Health Alerts.

    **Tags:** Health

    **Supported operations:** GET

    **Operation IDs:**

    - `getHealthAlertModel` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): Various filter criteria can be specified using the format `startTime:starttimeinsecs;endTime:endtimeinsecs;deviceUUIDs:Listofdeviceuuids;status:Listofstatuses;moduleIDs:Listof_moduleIDs.` `startTime` -- start time in unix format - startTime and endTime should be specified together `endTime` -- end time in unix format - startTime and endTime should be specified together `deviceUUIDs` -- List of device UUIDs (UUID is 0 for Firewall Management Center). `status` -- List of status codes to filter delimited by comma, e.g. green,red,yellow. `moduleIDs` -- List of module ids to filter, delimited by comma. .
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/health/alerts/{uuid}'
    SUPPORTED_FILTERS = ['start_time', 'end_time', 'device_uuids', 'status', 'module_ids']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670

    @utils.support_params
    def get(self, start_time=None, end_time=None, device_uuids=None, status=None, module_ids=None, params=None):
        return super().get(params=params)
