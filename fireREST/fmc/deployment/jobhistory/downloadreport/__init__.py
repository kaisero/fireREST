from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class DownloadReport(ChildResource):
    CONTAINER_NAME = 'JobHistory'
    CONTAINER_PATH = '/deployment/jobhistories/{uuid}'
    PATH = '/deployment/jobhistories/{container_uuid}/operational/downloadreports/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
