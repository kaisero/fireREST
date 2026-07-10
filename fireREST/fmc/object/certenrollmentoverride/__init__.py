from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import ChildResource


class CertEnrollmentOverride(ChildResource):
    """Get list of all certificate enrollment object overrides within the specified containerUUID.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getVpnCertEnrollmentOverride` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'CertEnrollment'
    CONTAINER_PATH = '/object/certenrollments/{uuid}'
    PATH = '/object/certenrollments/{container_uuid}/overrides'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
