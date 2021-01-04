from typing import Union

from fireREST import utils
from fireREST.fmc import ChildResource


class Deployment(ChildResource):
    CONTAINER_NAME = 'DeployableDevice'
    CONTAINER_PATH = '/deployment/deployabledevices/{uuid}'
    PATH = '/deployment/deployabledevices/{container_uuid}/deployments'
    SUPPORTED_FILTERS = ['start_time', 'end_time']
    SUPPORTED_PARAMS = []
    IGNORE_FOR_CREATE = []
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
