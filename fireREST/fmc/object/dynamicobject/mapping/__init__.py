from fireREST.fmc import ChildResource


class Mapping(ChildResource):
    CONTAINER_NAME = 'DynamicObject'
    CONTAINER_PATH = '/object/dynamicobjects/{uuid}'
    PATH = '/object/dynamicobjects/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '7.0.0'
