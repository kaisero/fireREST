from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class EmailReport(ChildResource):
    """Emails the report.

    **Tags:** Deployment

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createEmailReport` (CREATE)
    """

    CONTAINER_NAME = 'JobHistory'
    CONTAINER_PATH = '/deployment/jobhistories/{uuid}'
    PATH = '/deployment/jobhistories/{container_uuid}/operational/emailreports/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
