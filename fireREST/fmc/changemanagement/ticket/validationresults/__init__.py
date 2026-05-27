from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ValidationResults(ChildResource):
    """Retrieves validation result for the input ticket.

    **Tags:** Change Management

    **Supported operations:** GET

    **Operation IDs:**

    - `getTicketValidationResult` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'Ticket'
    CONTAINER_PATH = '/changemanagement/tickets/{uuid}'
    PATH = '/changemanagement/tickets/{container_uuid}/validationresults/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
