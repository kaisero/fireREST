from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class RadiusConfigObject(Resource):
    """Retrieves, creates, updates, or deletes RADIUS authentication configuration objects.

    **Tags:** User

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllRadiusConfigObject` (GET (list))
    - `getRadiusConfigObject` (GET)
    - `createRadiusConfigObject` (CREATE)
    - `updateRadiusConfigObject` (UPDATE)
    - `deleteRadiusConfigObject` (DELETE)
    """

    PATH = '/users/externalauths/authconfigobjects/radiusconfigobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_1000
