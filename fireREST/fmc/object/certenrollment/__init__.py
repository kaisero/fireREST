from fireREST.defaults import API_RELEASE_640, API_RELEASE_720
from fireREST.fmc import Resource


class CertEnrollment(Resource):
    """[DEV ERROR: Missing description]

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVpnCertEnrollmentModel` (GET (list))
    - `getVpnCertEnrollmentModel` (GET)
    - `createVpnCertEnrollmentModel` (CREATE)
    - `updateVpnCertEnrollmentModel` (UPDATE)
    - `deleteVpnCertEnrollmentModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/certenrollments/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720
