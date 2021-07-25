from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'AnyconnectCustomAttribute'
    CONTAINER_PATH = '/object/anyconnectcustomattributes/{uuid}'
    PATH = '/object/anyconnectcustomattributes/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
