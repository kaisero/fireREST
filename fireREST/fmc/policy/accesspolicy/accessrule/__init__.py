from fireREST.defaults import API_CONFIG_NAME
from fireREST.fmc import Connection, ChildResource


class AccessRule(ChildResource):
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/accessrules/{uuid}'
    SUPPORTED_OPERATIONS = ['create', 'get', 'update', 'delete']
