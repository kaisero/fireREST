from fireREST.fmc import ChildResource


class PendingChanges(ChildResource):
    CONTAINER_NAME = 'DeployableDevice'
    CONTAINER_PATH = '/deployment/deployabledevices/{uuid}'
    PATH = '/deployment/deployabledevices/{container_uuid}/pendingchanges'
    SUPPORTED_FILTERS = ['parent_entity_types', 'parent_uuid']
    SUPPORTED_PARAMS = []
    IGNORE_FOR_CREATE = []
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
