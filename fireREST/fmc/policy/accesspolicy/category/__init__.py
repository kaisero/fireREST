from typing import Union

from fireREST import utils
from fireREST.fmc import ChildResource


class Category(ChildResource):
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/categories/{uuid}'
    SUPPORTED_FILTERS = []
    SUPPORTED_PARAMS = ['below_category', 'above_category', 'section', 'insert_before', 'insert_after']
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
        after_category=None,
        before_category=None,
        section=None,
        insert_after=None,
        insert_before=None,
        params=None,
    ):
        return super().create(data=data, container_uuid=container_uuid, container_name=container_name, params=params)
