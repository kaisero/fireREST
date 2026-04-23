from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ValidationResults(ChildResource):
    CONTAINER_NAME = 'Ticket'
    CONTAINER_PATH = '/changemanagement/tickets/{uuid}'
    PATH = '/changemanagement/tickets/{container_uuid}/validationresults/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
