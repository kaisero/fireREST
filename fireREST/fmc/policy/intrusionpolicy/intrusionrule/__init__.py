from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import ChildResource


class IntrusionRule(ChildResource):
    """Retrieves the per-policy behaviour of the specified intrusion rule ID for the target intrusion policy ID.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllSnort3IPSRules` (GET (list))
    - `getSnort3IPSRules` (GET)
    - `updateMultipleSnort3IPSRules` (UPDATE (bulk))
    - `updateSnort3IPSRules` (UPDATE)

    **Query parameters:**

    - `filter` (string, optional): Value can be any of the formats (including quotes): `"gid:123;sid:456"` or `"overrides:true;ipspolicy:{uuid1,uuid2,...}` or `"fts:789"` or `"isSystemDefined:{true/false}"`. `ipspolicy` is a comma-separated list of Snort 3 Intrusion Policy IDs.
    - `sort` (string, optional): Sorting parameters to be provided e.g. sid,-sid,gid,-gid,msg,-msg.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk Snort 3 intrusion rule operations.
    """

    CONTAINER_NAME = 'IntrusionPolicy'
    CONTAINER_PATH = '/policy/intrusionpolicies/{uuid}'
    PATH = '/policy/intrusionpolicies/{container_uuid}/intrusionrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_670
