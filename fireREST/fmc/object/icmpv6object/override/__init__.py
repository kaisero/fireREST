from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Icmpv6Object'
    CONTAINER_PATH = '/object/icmpv6objects/{uuid}'
    PATH = '/object/icmpv6objects/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
