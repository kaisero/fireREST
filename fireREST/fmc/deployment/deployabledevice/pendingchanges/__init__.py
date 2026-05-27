from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource


class PendingChanges(ChildResource):
    """Retrieves all the policy and object changes for the selected device.

    **Tags:** Deployment

    **Supported operations:** GET

    **Operation IDs:**

    - `getPendingChanges` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): The filter criteria for which the details have to be fetched - Only works when "expanded" is set to "true". Examples: ParentEntityTypes:AccessPolicy, EntityUUID:0050568C-35A0-0ed3-0000-004294969351.To fetch the historical data pass the left and right job UUID. Example LeftJobUUID:4b9fe31c-34cc-11ea-8b36-8eb5492fc3a5;RightJobUUID:4b9fe31c-34cc-11ea-8b36-8eb5492fc3a3.For filter based on User add a filter using key word UserList.Example: UserList : user1,user2.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeployableDevice'
    CONTAINER_PATH = '/deployment/deployabledevices/{uuid}'
    PATH = '/deployment/deployabledevices/{container_uuid}/pendingchanges'
    SUPPORTED_FILTERS = ['parent_entity_types', 'parent_uuid']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
