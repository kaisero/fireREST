from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'KeyChain'
    CONTAINER_PATH = '/object/keychains/{uuid}'
    PATH = '/object/keychains/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.4.0'
