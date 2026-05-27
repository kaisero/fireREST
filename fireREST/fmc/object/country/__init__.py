from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class Country(Resource):
    """Retrieves the country object associated with the specified ID. If no ID is specified, retrieves list of all country objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllCountryObject` (GET (list))
    - `getCountryObject` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/countries/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
