from fireREST.fmc import ChildResource


class SecurityIntelligencePolicy(ChildResource):
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/securityintelligencepolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
