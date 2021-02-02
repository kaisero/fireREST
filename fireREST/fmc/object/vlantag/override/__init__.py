from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'VlanTag'
    CONTAINER_PATH = '/object/vlantags/{uuid}'
    PATH = '/object/vlantags/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
