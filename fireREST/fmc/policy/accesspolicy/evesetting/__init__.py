from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import ChildResource


class EveSetting(ChildResource):
    """Retrieves or updates EVE settings for the specified access policy.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllEveSetting` (GET (list))
    - `getEveSetting` (GET)
    - `updateEveSetting` (UPDATE)
    """

    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/evesettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
