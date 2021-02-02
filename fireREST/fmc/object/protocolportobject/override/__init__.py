from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'ProtocolPortObject'
    CONTAINER_PATH = '/object/protocolportobjects/{uuid}'
    PATH = '/object/protocolportobjects/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
