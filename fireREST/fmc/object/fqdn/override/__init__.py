from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Fqdn'
    CONTAINER_PATH = '/object/fqdns/{uuid}'
    PATH = '/object/fqdns/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.3.0'
