from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Connection, Resource
from fireREST.fmc.changemanagement.ticket.previewchanges import PreviewChanges
from fireREST.fmc.changemanagement.ticket.validationresults import ValidationResults


class Ticket(Resource):
    PATH = '/changemanagement/tickets/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.previewchanges = PreviewChanges(conn)
        self.validationresults = ValidationResults(conn)
