from fireREST.fmc import ChildResource


class IntrusionRuleGroup(ChildResource):
    CONTAINER_NAME = 'IntrusionPolicy'
    CONTAINER_PATH = '/policy/intrusionpolicies/{uuid}'
    PATH = '/policy/intrusionpolicies/{container_uuid}/intrusionrulegroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
