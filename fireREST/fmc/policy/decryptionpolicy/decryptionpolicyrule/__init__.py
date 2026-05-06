from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class DecryptionPolicyRule(ChildResource):
    """Retrieves the decryption policy rule associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDecryptionPolicyRule` (GET (list))
    - `getDecryptionPolicyRule` (GET)
    - `createDecryptionPolicyRule` (CREATE)
    - `updateDecryptionPolicyRule` (UPDATE)
    - `deleteDecryptionPolicyRule` (DELETE)

    **Query parameters:**

    - `insertAfter` (number, optional): This parameter specifies that the rule will be inserted after the specified rule index. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply.
    - `insertBefore` (number, optional): This parameter specifies that the rule will be inserted before the specified rule index. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply.
    - `category` (string, optional): This parameter specifies the category into which the rule will be added. If a category is specified it must exist or the request will fail.
    - `partialUpdate` (boolean, optional): This field specifies whether to change the entire object or only certain attributes of it. When its value is false the whole object will change, and if the value is true then only the attributes that are specified will change. The default value of this field is false.
    - `filter` (string, optional): Filter by full text search(fts) over all rule attributes is supported.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DecryptionPolicy'
    CONTAINER_PATH = '/policy/decryptionpolicies/{uuid}'
    PATH = '/policy/decryptionpolicies/{container_uuid}/decryptionpolicyrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
