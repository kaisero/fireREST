from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class DownloadReport(ChildResource):
    """Retrieves the report for download.

    **Tags:** Deployment

    **Supported operations:** GET

    **Operation IDs:**

    - `getDownloadReport` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'JobHistory'
    CONTAINER_PATH = '/deployment/jobhistories/{uuid}'
    PATH = '/deployment/jobhistories/{container_uuid}/operational/downloadreports/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
