from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Range'
    CONTAINER_PATH = '/object/ranges/{uuid}'
    PATH = '/object/ranges/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
