from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class UmbrellaDnsRule(ChildResource):
    """Retrieves the umbrella DNS Rule associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllUmbrellaDNSRule` (GET (list))
    - `getUmbrellaDNSRule` (GET)
    - `updateUmbrellaDNSRule` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'UmbrellaDnsPolicy'
    CONTAINER_PATH = '/policy/umbrelladnspolicies/{uuid}'
    PATH = '/policy/umbrelladnspolicies/{container_uuid}/umbrelladnsrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
