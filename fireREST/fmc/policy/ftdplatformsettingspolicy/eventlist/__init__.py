from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import ChildResource


class EventList(ChildResource):
    """Retrieves, creates, updates, or deletes syslog event lists for the specified FTD platform settings policy.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllEventList` (GET (list))
    - `getEventList` (GET)
    - `createEventList` (CREATE)
    - `updateEventList` (UPDATE)
    - `deleteEventList` (DELETE)
    """

    CONTAINER_NAME = 'FtdPlatformSettingsPolicy'
    CONTAINER_PATH = '/policy/ftdplatformsettingspolicies/{uuid}'
    PATH = '/policy/ftdplatformsettingspolicies/{container_uuid}/syslog/eventlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_770
