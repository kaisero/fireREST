from fireREST.fmc import Resource


class CloudEventsConfig(Resource):
    PATH = '/integration/cloudeventsconfigs/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.4.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.4.0'
