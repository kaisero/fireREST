from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import ChildResource


class EtherChannelInterface(ChildResource):
    """Retrieves the ethernet channel interface associated with the specified NGFW device ID and interface ID. If no ID is specified, retrieves list of all ethernet channel interfaces associated with the specified NGFW device ID. <div class="alert alert-warning">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDEtherChannelInterface` (GET (list))
    - `getFTDEtherChannelInterface` (GET)
    - `createFTDEtherChannelInterface` (CREATE)
    - `updateFTDEtherChannelInterface` (UPDATE)
    - `deleteFTDEtherChannelInterface` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/etherchannelinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
