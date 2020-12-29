from fireREST.fmc import Resource


class FilePolicy(Resource):
    PATH = '/policy/filepolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
