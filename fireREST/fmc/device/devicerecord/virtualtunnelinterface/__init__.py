from typing import Dict

from fireREST import utils
from fireREST.fmc import ChildResource


class VirtualTunnelInterface(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/virtualtunnelinterfaces/{uuid}'
    SUPPORTED_PARAMS = ['name']
    MINIMUM_VERSION_REQUIRED_CREATE = '6.7.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.7.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.7.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.7.0'

    @utils.support_params
    def get(self, container_uuid=None, container_name=None, uuid=None, name=None, params=None):
        return super().get(
            container_uuid=container_uuid, container_name=container_name, uuid=uuid, name=name, params=params
        )

    @utils.support_params
    def update(self, data: Dict, container_uuid=None, container_name=None, uuid=None, name=None, params=None):
        return super().update(
            container_uuid=container_uuid, container_name=container_name, uuid=uuid, name=name, params=params
        )

    @utils.support_params
    def delete(self, container_uuid=None, container_name=None, uuid=None, name=None, params=None):
        return super().get(
            container_uuid=container_uuid, container_name=container_name, uuid=uuid, name=name, params=params
        )
