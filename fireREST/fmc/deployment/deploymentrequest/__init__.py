from fireREST.fmc import Resource


class DeploymentRequest(Resource):
    PATH = '/deployment/deploymentrequests/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.1.0'
