from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Url'
    CONTAINER_PATH = '/object/urls/{uuid}'
    PATH = '/object/urls/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
