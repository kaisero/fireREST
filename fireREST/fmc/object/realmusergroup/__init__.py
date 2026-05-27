from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class RealmUserGroup(Resource):
    """Retrieves the realm user group object associated with the specified ID. If no ID is specified, retrieves list of all realm user group objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllRealmUserGroup` (GET (list))
    - `getRealmUserGroup` (GET)

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:name;realm:realm;userId:userId` `name` -- Name of the group to be queried starting with.... `realm` -- Realm uuid for the group. `userId` -- Groups with the user id.
    - `name` (string, optional): Name of the group to be queried starting with
    - `realm` (string, optional): Realm uuid for the group.
    - `userId` (string, optional): Groups with the user id.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/realmusergroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
