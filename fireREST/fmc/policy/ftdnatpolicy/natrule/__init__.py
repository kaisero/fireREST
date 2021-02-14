from typing import Dict, Union

from fireREST import utils
from fireREST.fmc import Connection, ChildResource


class NatRule(ChildResource):
    CONTAINER_NAME = 'FtdNatPolicy'
    CONTAINER_PATH = '/policy/ftdnatpolicies/{uuid}'
    PATH = '/policy/ftdnatpolicies/{container_uuid}/natrules/{uuid}'
    SUPPORTED_FILTERS = [
        'section',
        'source_interface',
        'destination_interface',
        'original_source',
        'original_destination',
        'translated_source',
        'translated_destination',
        'original_source_port',
        'original_destination_port',
        'translated_source_port',
        'translated_destination_port',
    ]
    SUPPORTED_PARAMS = []
    IGNORE_FOR_CREATE = []
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'

    @utils.support_params
    def get(
        self,
        container_uuid=None,
        container_name=None,
        uuid=None,
        name=None,
        source_interface=None,
        destination_interface=None,
        original_source=None,
        original_destination=None,
        translated_source=None,
        translated_destination=None,
        original_source_port=None,
        original_destination_port=None,
        translated_source_port=None,
        translated_destination_port=None,
        params=None,
    ):
        return super().get(
            container_uuid=container_uuid, container_name=container_name, name=name, uuid=uuid, params=params
        )
