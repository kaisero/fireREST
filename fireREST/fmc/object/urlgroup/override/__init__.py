from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'UrlGroup'
    CONTAINER_PATH = '/object/urlgroups/{uuid}'
    PATH = '/object/urlgroups/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
