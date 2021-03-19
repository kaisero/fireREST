from fireREST.fmc import Resource


class RouteMap(Resource):
    PATH = '/object/routemaps/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
