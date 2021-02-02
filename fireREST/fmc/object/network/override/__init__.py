from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Network'
    CONTAINER_PATH = '/object/networks/{uuid}'
    PATH = '/object/networks/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
