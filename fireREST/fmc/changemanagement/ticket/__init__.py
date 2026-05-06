from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Connection, Resource
from fireREST.fmc.changemanagement.ticket.previewchanges import PreviewChanges
from fireREST.fmc.changemanagement.ticket.validationresults import ValidationResults


class Ticket(Resource):
    """Retrieves all the tickets for the logged in user.

    **Tags:** Change Management

    **Supported operations:** GET, CREATE, UPDATE

    **Operation IDs:**

    - `getAllTicket` (GET (list))
    - `getTicket` (GET)
    - `createTicket` (CREATE)
    - `updateTicket` (UPDATE)

    **Query parameters:**

    - `history` (boolean, optional): Boolean identifier to fetch ticket history or ignore history. `false` is the default value.
    - `filter` (string, optional): To filter by state of ticket use : `State:NEW`. For multiple states `State:NEW,IN_PROGRESS`
    - `allUsers` (boolean, optional): To get tickets of other users too. User has to have review tickets permission to use this as true.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/changemanagement/tickets/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.previewchanges = PreviewChanges(conn)
        self.validationresults = ValidationResults(conn)
