from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'DnsServerGroup'
    CONTAINER_PATH = '/object/dnsservergroups/{uuid}'
    PATH = '/object/dnsservergroups/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
