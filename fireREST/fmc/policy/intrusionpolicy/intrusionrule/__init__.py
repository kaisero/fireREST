from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import ChildResource


class IntrusionRule(ChildResource):
    CONTAINER_NAME = 'IntrusionPolicy'
    CONTAINER_PATH = '/policy/intrusionpolicies/{uuid}'
    PATH = '/policy/intrusionpolicies/{container_uuid}/intrusionrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_670
