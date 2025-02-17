from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Ipv4AddressPool'
    CONTAINER_PATH = '/object/ipv4addresspools/{uuid}'
    PATH = '/object/ipv4addresspools/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
