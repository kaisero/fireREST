from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import Resource


class CloudEventsConfig(Resource):
    PATH = '/integration/cloudeventsconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
