from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class RealmUser(Resource):
    """Retrieves the realm user object associated with the specified ID. If no ID is specified, retrieves list of all realm user objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllRealmUser` (GET (list))
    - `getRealmUser` (GET)

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:name;realm:realm;groupId:groupId;resolved:resolved` `name` -- Name of the user to be queried starting with... `realm` -- Realm uuid for the user. `groupId` -- Users with the group id. `resolved` -- Either `true` or `false`.
    - `name` (string, optional): Name of the user to be queried starting with.
    - `realm` (string, optional): Realm uuid for the user.
    - `resolved` (string, optional): Either `true` or `false`.
    - `groupId` (string, optional): Users with the group id.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/realmusers/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
