from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ConfigChanges(Resource):
    """Retrieves the configuration changes associated with audit.

    **Tags:** Audit

    **Supported operations:** GET

    **Operation IDs:**

    - `getAuditConfigChanges` (GET (list))

    **Query parameters:**

    - `auditLogId` (string): Unique identifier for Audit Log.
    - `snapshotId` (string): Unique identifier for Audit Snapshot.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    NAMESPACE = 'platform_with_domain'
    PATH = '/audit/configchanges/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
