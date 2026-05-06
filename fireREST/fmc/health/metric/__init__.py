from fireREST import utils
from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class Metric(Resource):
    """Retrieves HealthMonitor metrics for the device.

    **Tags:** Health

    **Supported operations:** GET

    **Operation IDs:**

    - `getHealthMetric` (GET (list))

    **Query parameters:**

    - `filter` (string): Various filter criteria can be specified using the format `deviceUUIDs:uuid1,uuid2;metric:metricname;startTime:starttimeinsecs;endTime:endtimeinsecs;step:stepinsecs;regexFilter:filteronmetric` `deviceUUIDs` --List UUID of the device to be queried. `metric` -- name of the prometheus metric to be queried. `startTime` -- start time in unix format seconds. `endTime` -- end time in unix format seconds. `step` -- step interval in seconds over which the data is returned. `regexFilter` -- filter to be applied on the metric names. Supports GO style regex e.g snort.&#42;&#124;lina.&#42; `queryFunction` -- optional query function which has to be applied to the query, can be one of `"avg", "rate", "min", "max"` `rateFunctionInterval` -- optional interval which has to be applied to the rate function, for e.g five minutes should be specified as `5m` . For e.g. to query all the memory metrics for LINA the filter parameter should be `deviceUUID:&lt;uuid&gt;;metric:mem;startTime:&lt;time&gt;;endTime:&lt;time&gt;;step:60;regexFilter:usedpercentage_lina`
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
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
