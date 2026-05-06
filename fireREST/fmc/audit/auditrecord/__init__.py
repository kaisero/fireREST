from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class AuditRecord(Resource):
    """Retrieves the audit record associated with the specified ID.

    **Tags:** Audit

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllAuditModel` (GET (list))
    - `getAuditModel` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    NAMESPACE = 'platform_with_domain'
    PATH = '/audit/auditrecords/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
