from fireREST.fmc import ChildResource


class InspectorConfig(ChildResource):
    CONTAINER_NAME = 'NetworkAnalysisPolicy'
    CONTAINER_PATH = '/policy/intrusionpolicies/{uuid}'
    PATH = '/policy/networkanalysispolicies/{container_uuid}/inspectorconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
