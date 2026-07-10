from fireREST.defaults import API_RELEASE_720, API_RELEASE_760
from fireREST.fmc import Resource


class HealthPolicy(Resource):
    """Retrieves, creates, updates, or deletes health policies.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllHealthPolicy` (GET (list))
    - `getHealthPolicy` (GET)
    - `createHealthPolicy` (CREATE)
    - `updateHealthPolicy` (UPDATE)
    - `deleteHealthPolicy` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:policyname` `policyname` -- Name of the Health Policy to be queried.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/healthpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760
