from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class SecurityZone(Resource):
    """Retrieves, deletes, creates, or modifies the security zone objects associated with the specified ID. If no ID is specified for a GET, retrieves list of all security zone objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSecurityZoneObject` (GET (list))
    - `getSecurityZoneObject` (GET)
    - `createMultipleSecurityZoneObject` (CREATE)
    - `updateSecurityZoneObject` (UPDATE)
    - `deleteSecurityZoneObject` (DELETE)

    **Query parameters:**

    - `groupByDevice` (string, optional): Set true to group interfaces by device and return as `devices` attribute, instead of `interfaces`.
    - `filter` (string, optional): Query Param to return security zones of specified InterfaceMode type based on the filter. Value is of format `interfaceMode:ROUTED or interfaceMode:PASSIVE or interfaceMode:INLINE or interfaceMode:SWITCHED or interfaceMode:ASA`.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for security zone objects.
    """

    PATH = '/object/securityzones/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
