from fireREST.fmc import ChildResource


class IntrusionRule(ChildResource):
    CONTAINER_NAME = 'IntrusionPolicy'
    CONTAINER_PATH = '/policy/intrusionpolicies/{uuid}'
    PATH = '/policy/intrusionpolicies/{container_uuid}/intrusionrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.7.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.7.0'
