from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class HealthPolicy(Resource):
    """Retrieves the Health Policy with the associated ID.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllHealthPolicy` (GET (list))
    - `getHealthPolicy` (GET)

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:policyname` `policyname` -- Name of the Health Policy to be queried.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/healthpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
