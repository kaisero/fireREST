from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class DeploymentRequest(Resource):
    PATH = '/deployment/deploymentrequests/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
