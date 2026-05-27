from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource


class Deployment(ChildResource):
    """Retrieves Deployment details for device

    **Tags:** Deployment

    **Supported operations:** GET

    **Operation IDs:**

    - `getDeploymentDetail` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): Value is of format `startTime:starttimeinsecs;endTime:endtimeinsecs;`. `startTime` -- start time in unix format (in seconds). startTime and endTime should be specified together. `endTime` -- end time in unix format (in seconds). startTime and endTime should be specified together.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeployableDevice'
    CONTAINER_PATH = '/deployment/deployabledevices/{uuid}'
    PATH = '/deployment/deployabledevices/{container_uuid}/deployments'
    SUPPORTED_FILTERS = ['start_time', 'end_time']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
