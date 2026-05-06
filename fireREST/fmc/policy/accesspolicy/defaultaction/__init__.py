from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import ChildResource


class DefaultAction(ChildResource):
    """Retrieves the default action associated with the specified access control policy ID and default action ID.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllDefaultAction` (GET (list))
    - `getDefaultAction` (GET)
    - `updateDefaultAction` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/defaultactions/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
