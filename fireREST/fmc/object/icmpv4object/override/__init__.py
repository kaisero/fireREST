from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Icmpv4Object'
    CONTAINER_PATH = '/object/icmpv4objects/{uuid}'
    PATH = '/object/icmpv4objects/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
