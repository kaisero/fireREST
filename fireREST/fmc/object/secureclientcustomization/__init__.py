from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class SecureClientCustomization(Resource):
    """Retrieves, update, deletes or creates Secure Client Customization. If no ID is specified for a GET, retrieves list of all AnyConnect Customization Objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSecureClientCustomizationModel` (GET (list))
    - `getSecureClientCustomizationModel` (GET)
    - `createSecureClientCustomizationModel` (CREATE)
    - `updateSecureClientCustomizationModel` (UPDATE)
    - `deleteSecureClientCustomizationModel` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/secureclientcustomizations/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
