from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class DeploymentRequest(Resource):
    """Creates a request for deploying configuration changes to devices.

    **Tags:** Deployment

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createDeploymentRequest` (CREATE)
    """

    PATH = '/deployment/deploymentrequests/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
