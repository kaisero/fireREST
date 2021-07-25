from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Ipv6AddressPool'
    CONTAINER_PATH = '/object/ipv6addresspools/{uuid}'
    PATH = '/object/ipv6addresspools/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
