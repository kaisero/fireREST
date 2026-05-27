from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class IseSecurityGroupTag(Resource):
    """Retrieves the ISE security group tag object with the specified ID. If no ID is specified, retrieves list of all ISE security group tag objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllISESecurityGroupTag` (GET (list))
    - `getISESecurityGroupTag` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/isesecuritygrouptags/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
