from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import Resource


class AggregateMetric(Resource):
    """Get metrics related to the health of the device and interface attributes.

    **Tags:** Health

    **Supported operations:** GET

    **Operation IDs:**

    - `getAggregateMetrics` (GET (list))

    **Query parameters:**

    - `filter` (string): Metrics are governed by health policies deployed on the FTD. If the health module is disabled, there is a chance that metric data wont be available or is incomplete. Filter criteria can be specified using the format `deviceuuid:deviceUuid; metric:metricname; timeRange:range.` `deviceuuid` -- Identifier for device. There can only be one device offered per request. This is a mandatory parameter in the filter query. `metric` -- Indicates the metric to be queried. Possible values are CPU, MEM, INTERFACE, DISKSTATS, CHASSISSTATS and HAINFO. If this filter is not used, all available metrics are retrieved. `timeRange` -- Enum which aids in retrieving the average metrics for time intervals. Possible values are 5m, 15m, 30m, and 1h. If this filter is not used, the average of the last five minutes will be shown by default.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/health/aggregatemetrics'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
