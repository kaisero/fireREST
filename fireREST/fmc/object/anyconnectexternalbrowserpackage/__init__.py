from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class AnyconnectExternalBrowserPackage(Resource):
    """Retrieves, update, deletes or creates the AnyConnect External Browser Package associated with the specified ID. If no ID is specified for a GET, retrieves list of all AnyConnect External Browser Package objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllAnyConnectExternalBrowserPackageModel` (GET (list))
    - `getAnyConnectExternalBrowserPackageModel` (GET)
    - `createAnyConnectExternalBrowserPackageModel` (CREATE)
    - `updateAnyConnectExternalBrowserPackageModel` (UPDATE)
    - `deleteAnyConnectExternalBrowserPackageModel` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/anyconnectexternalbrowserpackages/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720
