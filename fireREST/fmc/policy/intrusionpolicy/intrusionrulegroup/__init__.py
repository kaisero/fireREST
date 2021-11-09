from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class IntrusionRuleGroup(ChildResource):
    CONTAINER_NAME = 'IntrusionPolicy'
    CONTAINER_PATH = '/policy/intrusionpolicies/{uuid}'
    PATH = '/policy/intrusionpolicies/{container_uuid}/intrusionrulegroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
