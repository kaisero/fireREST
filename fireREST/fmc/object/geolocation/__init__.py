from fireREST.defaults import API_RELEASE_700, API_RELEASE_610
from fireREST.fmc import Resource


class GeoLocation(Resource):
    """Retrieves, deletes, creates, or modifies the geolocation object associated with the specified ID. If no ID is specified, retrieves list of all geolocation objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllGeoLocationObject` (GET (list))
    - `getGeoLocationObject` (GET)
    - `createGeoLocationObject` (CREATE)
    - `updateGeoLocationObject` (UPDATE)
    - `deleteGeoLocationObject` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/geolocations/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700
