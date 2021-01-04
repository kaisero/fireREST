from fireREST.fmc import Resource


class GeoLocation(Resource):
    PATH = '/object/geolocations/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
