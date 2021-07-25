from fireREST.fmc import ChildResource


class InspectorOverrideConfig(ChildResource):
    CONTAINER_NAME = 'NetworkAnalysisPolicy'
    CONTAINER_PATH = '/policy/networkanalysispolicies/{uuid}'
    PATH = '/policy/networkanalysispolicies/{container_uuid}/inspectoroverrideconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
