from typing import Union

from fireREST import utils
from fireREST.fmc import ChildResource


class PrefilterRule(ChildResource):
    CONTAINER_NAME = 'PrefilterPolicy'
    CONTAINER_PATH = '/policy/prefilterpolicies/{uuid}'
    PATH = '/policy/prefilterpolicies/{container_uuid}/prefilterrules/{uuid}'
    SUPPORTED_FILTERS = []
    SUPPORTED_PARAMS = ['category', 'section', 'insert_before', 'insert_after']
    IGNORE_FOR_CREATE = []
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_CREATE = '6.5.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.5.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.5.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.5.0'

    @utils.support_params
    def create(
        self,
        data: Union[dict, list],
        container_uuid=None,
        container_name=None,
        category=None,
        section=None,
        insert_after=None,
        insert_before=None,
        params=None,
    ):
        return super().create(data=data, container_uuid=container_uuid, container_name=container_name, params=params)
