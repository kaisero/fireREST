from fireREST.fmc import ChildResource


class BlockDnsRule(ChildResource):
    CONTAINER_NAME = 'DnsPolicy'
    CONTAINER_PATH = '/policy/dnspolicies/{uuid}'
    PATH = '/policy/dnspolicies/{container_uuid}/blockdnsrule/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
