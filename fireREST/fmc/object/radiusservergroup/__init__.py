from fireREST.fmc import Resource


class RadiusServerGroup(Resource):
    PATH = '/object/radiusservergroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
