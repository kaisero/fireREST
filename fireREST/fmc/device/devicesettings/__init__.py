from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class DeviceSettings(Resource):
    PATH = '/devices/devicesettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
