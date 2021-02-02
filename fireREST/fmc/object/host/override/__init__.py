from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Host'
    CONTAINER_PATH = '/object/hosts/{uuid}'
    PATH = '/object/hosts/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
