from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import ChildResource


class DefaultAction(ChildResource):
    """Retrieves the default action associated with the specified prefilter control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified prefilter policy ID.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllPrefilterDefaultAction` (GET (list))
    - `getPrefilterDefaultAction` (GET)
    - `updatePrefilterDefaultAction` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'PrefilterPolicy'
    CONTAINER_PATH = '/policy/prefilterpolicies/{uuid}'
    PATH = '/policy/prefilterpolicies/{container_uuid}/defaultactions/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_650
