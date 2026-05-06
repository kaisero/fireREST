from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class PreviewChanges(ChildResource):
    """Retrieves ticket based changes

    **Tags:** Change Management

    **Supported operations:** GET

    **Operation IDs:**

    - `getTicketPreviewChange` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): The filter criteria for which the details have to be fetched - Only works when "expanded" is set to "true". Examples: ParentEntityTypes:AccessPolicy, EntityUUID:0050568C-35A0-0ed3-0000-004294969351.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'Ticket'
    CONTAINER_PATH = '/changemanagement/tickets/{uuid}'
    PATH = '/changemanagement/tickets/{container_uuid}/previewchanges/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
