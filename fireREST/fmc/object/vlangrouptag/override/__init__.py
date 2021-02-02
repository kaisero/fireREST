from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'VlanGroupTag'
    CONTAINER_PATH = '/object/vlangrouptags/{uuid}'
    PATH = '/object/vlangrouptags/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
