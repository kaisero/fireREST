from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Connection, Resource
from fireREST.fmc.deployment.jobhistory.downloadreport import DownloadReport
from fireREST.fmc.deployment.jobhistory.emailreport import EmailReport


class JobHistory(Resource):
    PATH = '/deployment/jobhistories/{uuid}'
    SUPPORTED_FILTERS = ['device_uuid']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.downloadreport = DownloadReport(conn)
        self.emailreport = EmailReport(conn)
