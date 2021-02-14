from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'TimeZone'
    CONTAINER_PATH = '/object/timezoneobjects/{uuid}'
    PATH = '/object/timezoneobjects/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
