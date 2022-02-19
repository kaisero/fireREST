from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class InspectorConfig(ChildResource):
    CONTAINER_NAME = 'NetworkAnalysisPolicy'
    CONTAINER_PATH = '/policy/intrusionpolicies/{uuid}'
    PATH = '/policy/networkanalysispolicies/{container_uuid}/inspectorconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
