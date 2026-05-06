from fireREST import utils
from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class IntrusionRule(Resource):
    """Retrieves, deletes, creates, or modifies Snort 3 intrusion rule associated with the specified ID. If no ID is specified for a GET, retrieves list of all Snort 3 intrusion rules.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSnort3IPSRulesObject` (GET (list))
    - `getSnort3IPSRulesObject` (GET)
    - `createMultipleSnort3IPSRulesObject` (CREATE)
    - `updateMultipleSnort3IPSRulesObject` (UPDATE (bulk))
    - `updateSnort3IPSRulesObject` (UPDATE)
    - `deleteMultipleSnort3IPSRulesObject` (DELETE (bulk))
    - `deleteSnort3IPSRulesObject` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Value can be any of the formats (including quotes): `"gid:123;sid:456"` or `"overrides:true;ipspolicy:{uuid1,uuid2,...}` or `"fts:789"` or `"isSystemDefined:{true/false}"`. `ipspolicy` is a comma-separated list of Snort 3 Intrusion Policy IDs.
    - `sort` (string, optional): Sorting parameters to be provided e.g. sid,-sid,gid,-gid,msg,-msg.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk Snort 3 intrusion rule operations.
    """
    PATH = '/object/intrusionrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700

    SUPPORTED_FILTERS = ['gid', 'sid', 'overrides', 'ips_policy', 'fts']

    @utils.support_params
    def get(self, uuid=None, name=None, gid=None, sid=None, overrides=None, ips_policy=None, fts=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
