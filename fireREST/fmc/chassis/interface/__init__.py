from typing import Dict, Optional

from fireREST import utils
from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import ChildResource


class Interface(ChildResource):
    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/chassisinterfaces/{uuid}'
    SUPPORTED_PARAMS = ['operation']

    @utils.minimum_version_required(version=API_RELEASE_710)
    @utils.resolve_by_name
    def evaluate_operation(
        self,
        operation: Optional[str] = None,
        container_uuid: Optional[str] = None,
        container_name: Optional[str] = None,
        uuid: Optional[str] = None,
        name: Optional[str] = None,
        params: Optional[Dict] = None,
    ):
        url = self.url(f'{self.PATH.format(container_uuid=container_uuid, uuid=uuid)}/evaluateoperation')
        return self.conn.get(url=url, params=params)
