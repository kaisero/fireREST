from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Connection, Resource
from fireREST.fmc.deployment.jobhistory.downloadreport import DownloadReport
from fireREST.fmc.deployment.jobhistory.emailreport import EmailReport


class JobHistory(Resource):
    """Retrieves the specified deployment job.

    **Tags:** Deployment

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllJobHistory` (GET (list))
    - `getJobHistory` (GET)
    - `updateJobHistory` (UPDATE)

    **Query parameters:**

    - `filter` (string, optional): Various filter criteria can be specified using the format `deviceUUID:{uuid};startTime:starttimeinsecs;endTime:endtimeinsecs;rollbackApplicable:trueorfalse;status:jobstatus;jobType:jobtype`. `startTime` -- start time in unix format (in seconds). startTime and endTime should be specified together. `endTime` -- end time in unix format (in seconds). startTime and endTime should be specified together. `rollbackApplicable` -- true/false. Not a mandatory field. `status` -- {DEPLOYING, DEPLOYED, FAILED, ABORTED, EDIT_INUSE}. Not a mandatory field. `jobType` -- {DEPLOYMENT, ROLLBACK, CERTIFICATE}. Not a mandatory field.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/deployment/jobhistories/{uuid}'
    SUPPORTED_FILTERS = ['device_uuid']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.downloadreport = DownloadReport(conn)
        self.emailreport = EmailReport(conn)
