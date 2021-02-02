from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'NetworkGroup'
    CONTAINER_PATH = '/object/networkgroups/{uuid}'
    PATH = '/object/networkgroups/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
