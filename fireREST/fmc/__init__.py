# -*- coding: utf-8 -*-

import json
import logging
import simplejson
from http.client import responses as http_responses
from typing import Dict, Union
from urllib.parse import urlencode

import requests
import urllib3
from packaging import version
from requests.auth import HTTPBasicAuth

from fireREST import defaults
from fireREST import exceptions as exc
from fireREST import utils

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Connection:

    """API Connection object used to interact with Firepower Management Center REST API"""

    def __init__(
        self,
        hostname: str,
        username: str,
        password: str,
        protocol=defaults.API_PROTOCOL,
        verify_cert=False,
        domain=defaults.API_DEFAULT_DOMAIN,
        timeout=defaults.API_REQUEST_TIMEOUT,
        dry_run=defaults.DRY_RUN,
    ):
        """Initialize connection object. It is highly recommended to use a
        dedicated user for api operations

        :param hostname: ip address or fqdn of firepower management center
        :type hostname: str
        :param username: username used for api authentication
        :type username: str
        :param password: password used for api authentication
        :type password: str
        :param protocol: protocol used to access fmc rest api. Defaults to `https`
        :type protocol: str, optional
        :param verify_cert: check https certificate for validity. Defaults to `False`
        :type verify_cert: bool, optional
        :param domain: name of the domain to access. Defaults to `Global`
        :type domain: str
        :param timeout: timeout value for http requests. Defaults to `120` seconds
        :type timeout: int, optional
        :param dry_run: only log POST,PUT and DELETE api calls
        :type dry_run: bool, optional
        """
        if not verify_cert:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers = {
            'Content-Type': defaults.API_CONTENT_TYPE,
            'Accept': defaults.API_CONTENT_TYPE,
            'User-Agent': defaults.API_USER_AGENT,
        }
        self.cred = HTTPBasicAuth(username, password)
        self.hostname = hostname
        self.protocol = protocol
        self.refresh_counter = defaults.API_REFRESH_COUNTER_INIT
        self.session = requests.Session()
        self.timeout = timeout
        self.dry_run = dry_run
        self.verify_cert = verify_cert
        self.domains = None
        self.login()
        self.domain = {'id': self.get_domain_id(domain), 'name': domain}
        self.version = self.get_version()

    @utils.handle_errors
    def _request(self, method: str, url: str, params=None, auth=None, data=None):
        """Base operation used for all http api calls to firepower management center

        :param method: http operation (post, get, put, delete)
        :type method: str
        :param url: url to api resource
        :type url: str
        :param params: additional http params that should be passed to the request
        :type params: dict, optional
        :param auth: credentials in base64 format
        :type auth: HTTPBasicAuth, optional
        :param data: request body (api payload)
        :type data: dict, optional
        :return: api response
        :rtype: requests.Response
        """
        params = utils.fix_params(params)
        response = None
        # dry_run only affects PUT, POST and DELETE operations
        # dry_run is not applicable for authentication related operations (login/refresh)
        if self.dry_run and method.lower() != 'get' and '/v1/auth/' not in url:
            msg = {
                'method': method.upper(),
                'url': url,
                'params': urlencode(params) if params else '',
                'data': data if data else '',
                'dry_run': True,
            }
            logger.info(msg)
        else:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=json.dumps(data),
                auth=auth,
                headers=self.headers,
                timeout=self.timeout,
                verify=self.verify_cert,
            )
            msg = {
                'method': method.upper(),
                'url': url,
                'params': urlencode(params) if params else '',
                'data': data if data else '',
                'status': f'{http_responses[response.status_code]} ({response.status_code})',
            }
            if response.status_code >= 400:
                logger.error('\n%s', json.dumps(msg, indent=4))
            else:
                logger.info('\n%s', json.dumps(msg, indent=4))
                try:
                    logger.debug('\n"response": %s', json.dumps(response.json(), sort_keys=True, indent=4))
                except json.JSONDecodeError:
                    pass
                except simplejson.errors.JSONDecodeError:
                    pass
        return response

    def get(self, url: str, params=None, _items=None):
        """GET operation with pagination support. If multiple requests are required to
        get all items responses are squashed a single response

        :param url: path to resource that will be queried
        :type url: str
        :param params: dict of parameters for http request. Defaults to `None`
        :type params: dict, optional
        :param _items: list of items if response includes multiple pages. Used internally for recursion
        :type _items: list, optional
        :return: dictionary or list of returned api objects
        :rtype: Union[dict, list]
        """
        if not utils.is_getbyid_operation(url) and _items is None:
            if params is None:
                params = {}
            if 'limit' not in params:
                params['limit'] = defaults.API_PAGING_LIMIT
            if 'expanded' not in params:
                params['expanded'] = defaults.API_EXPANSION_MODE

        response = self._request('get', url, params=params)
        payload = response.json()

        if 'paging' in payload:
            if _items is None:
                _items = []
            if 'items' in payload:
                _items.extend(payload['items'])
                if 'next' in payload['paging']:
                    _items = self.get(payload['paging']['next'][0], params=None, _items=_items)
            return _items
        return payload

    def delete(self, url: str, params=None):
        """DELETE specified api resource

        :param url: path to resource that will be deleted
        :type url: str
        :param params: dict of parameters for http request
        :type params: dict, optional
        :return: api response
        :rtype: requests.Response
        """
        return self._request('delete', url, params=params)

    def post(self, url: str, data: Dict, params=None, ignore_fields=None):
        """POST operation that is mostly used to create new resources or trigger tasks

        :param url: path to resource on which POST operation will be performed
        :type url: str
        :param data: data that will be sent to the api endpoint
        :type data: Union[list, dict], optional
        :param params: dict of parameters for http request
        :type params: dict, optional
        :param ignore_fields: list of fields that should be stripped from payload before performing operation
        :type ignore_fields: list, optional
        :return: requests.response object
        """
        data = utils.sanitize_payload('post', data, ignore_fields)
        return self._request('post', url, params=params, data=data)

    def put(self, url: str, data: Dict, params=None, ignore_fields=None):
        """PUT operation that updates existing resources according to the payload provided

        :param url: path to resource on which POST operation will be performed
        :type url: str
        :param data: data that will be sent to the api endpoint
        :type data: Union[list, dict], optional
        :param params: dict of parameters for http request
        :type params: dict, optional
        :param ignore_fields: list of fields that should be stripped from payload before performing operation
        :type ignore_fields: list, optional
        :return: api response
        :rtype: requests.Response
        """
        data = utils.sanitize_payload('put', data, ignore_fields)
        return self._request('put', url, data=data, params=params)

    def login(self):
        """Basic authentication to firepower management center rest api
        in case authentication is successful an access and refresh token will be saved to
        the `Connection` object. Subsequent api calls will be performed using the access token

        """
        logger.info('Attempting authentication with Firepower Management Center (%s)', self.hostname)
        url = f'{self.protocol}://{self.hostname}{defaults.API_AUTH_URL}'
        response = self._request('post', url, auth=self.cred)
        self.headers['X-auth-access-token'] = response.headers['X-auth-access-token']
        self.headers['X-auth-refresh-token'] = response.headers['X-auth-refresh-token']
        self.domains = json.loads(response.headers['DOMAINS'])
        self.refresh_counter = defaults.API_REFRESH_COUNTER_INIT

    def refresh(self):
        """Refresh authorization token. This operation is performed for up to three
        times, afterwards a re-authentication using `self.login()` will be performed

        """
        if self.refresh_counter < defaults.API_REFRESH_COUNTER_MAX:
            logger.info('Access token is invalid. Refreshing authentication token')
            self.refresh_counter += 1
            url = f'{self.protocol}://{self.hostname}{defaults.API_REFRESH_URL}'
            response = self._request('post', url)
            self.headers['X-auth-access-token'] = response.headers['X-auth-access-token']
            self.headers['X-auth-refresh-token'] = response.headers['X-auth-refresh-token']

        else:
            logger.info('Maximum number of authentication refresh operations reached', self.hostname)
            self.login()

    def get_version(self):
        """Get version of fmc

        :return: server version of firepower management center
        :rtype: version.Version
        """
        url = f'{self.protocol}://{self.hostname}{defaults.API_PLATFORM_URL}/info/serverversion'
        return version.parse(self._request('get', url).json()['items'][0]['serverVersion'].split(' ')[0])

    def get_domain_id(self, name: str):
        """helper function to retrieve domain id from list of domains

        :param name: name of the domain
        :type name: str
        :return: domain uuid
        :rtype: str
        """
        for domain in self.domains:
            if domain['name'] == name:
                return domain['uuid']

        domains = ', '.join((domain['name'] for domain in self.domains))
        msg = f'Could not find domain with name {name}. Available Domains: {domains}'
        raise exc.DomainNotFoundError(msg=msg)


class Resource:
    """Base class for api resources. `Resource` can be used for all api resources
    that are not part of another container. A valid example would be an AccessPolicy
    an invalid example would be an AccessRule which existing within a container (AccessPolicy

    """

    # namespace of api resource. options: base, config, platform, refresh
    NAMESPACE = 'config'
    # path to api resource within a namespace. e.g. /policy/accesspolicy
    PATH = '/'
    # supported filter arguments for GET operations
    SUPPORTED_FILTERS = []
    # supported param arguments for operations
    SUPPORTED_PARAMS = []
    # ignore fields for create operations
    IGNORE_FOR_CREATE = []
    # ignore fields for put operations
    IGNORE_FOR_UPDATE = []
    # minimum version required for create()
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    # minimum version required for get()
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    # minimum version required for update()
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    # minimum version required for delete()
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'

    def __init__(
        self, conn,
    ):
        """Initialize Resource object

        :param conn: connection object used for api calls
        :type conn: fireREST.fmc.Connection
        """
        self.conn = conn
        self.version = conn.version

    def url(self, path, namespace=None):
        """Generate url for requests to fmc rest api

        :param path: relative path to api resource
        :type path: str
        :param namespace: namespace to which api call should be routed
        :type namespace: str, optional
        :return: formatted url used for api call
        :rtype: str
        """
        if not namespace:
            namespace = self.NAMESPACE
        options = {
            'base': f'{self.conn.protocol}://{self.conn.hostname}{path}',
            'config': f'{self.conn.protocol}://{self.conn.hostname}{defaults.API_CONFIG_URL}/domain/'
            f'{self.conn.domain["id"]}{path}',
            'platform': f'{self.conn.protocol}://{self.conn.hostname}{defaults.API_PLATFORM_URL}{path}',
            'tid': f'{self.conn.protocol}://{self.conn.hostname}{defaults.API_TID_URL}{path}',
            'refresh': f'{self.conn.protocol}://{self.conn.hostname}{defaults.API_REFRESH_URL}',
        }
        if namespace not in options.keys():
            raise exc.InvalidNamespaceError(f'Invalid namespace "{namespace}" provided. Options: {options.keys()}')
        return utils.fix_url(options[namespace])

    @utils.minimum_version_required
    def create(self, data: Union[dict, list], params=None):
        """Create api resource
        :param data: data that will be sent to the api endpoint
        :type data: Union[list, dict], optional
        :param params: dict of parameters for http request
        :type params: dict, optional
        :return: api response
        :rtype: requests.Response
        """
        url = self.url(self.PATH.format(uuid=None))
        return self.conn.post(url, data, params, self.IGNORE_FOR_CREATE)

    @utils.resolve_by_name
    @utils.minimum_version_required
    def get(self, uuid=None, name=None, params=None):
        """Get api resource in json format. If no name or uuid is provided
        a list of all available resources will be returned

        :param uuid: id of resource
        :type uuid: str, optional
        :param name: name of resource
        :type name: str, optional
        :param params: dict of parameters for http request
        :type params: dict, optional
        :return: api response
        :rtype: Union[dict, list]
        """
        url = self.url(self.PATH.format(uuid=uuid))
        return self.conn.get(url, params)

    @utils.minimum_version_required
    def update(self, data: Dict, params=None):
        """Update existing api resource. Existing data will be overridden with
        the provided payload. The request will be routed to the correct resource
        by extracting the `id` within the payload

        :param data: data that will be sent to the api endpoint
        :type data: Union[list, dict], optional
        :param params: dict of parameters for http request
        :type params: dict, optional
        :return: api response
        :rtype: requests.Response
        """
        url = self.url(self.PATH.format(uuid=data['id']))
        return self.conn.put(url, data, params, self.IGNORE_FOR_UPDATE)

    @utils.resolve_by_name
    @utils.minimum_version_required
    def delete(self, uuid=None, name=None):
        """Delete existing api resource. Either `name` or `uuid` must
        be provided to delete an existing resource

        :param uuid: id of resource
        :type uuid: str, optional
        :param name: name of resource
        :type name: str, optional
        :return: api response
        :rtype: requests.Response
        """
        url = self.url(self.PATH.format(uuid=uuid))
        return self.conn.delete(url)


class ChildResource(Resource):
    """Base class for api resources located within a container"""

    # name of container class that hosts the ChildResource
    CONTAINER_NAME = 'Resource'

    # path to container class that hosts the ChildResource
    CONTAINER_PATH = '/'

    @utils.resolve_by_name
    @utils.minimum_version_required
    def create(self, data: Union[dict, list], container_uuid=None, container_name=None, params=None):
        """Create api resource. Either name or uuid of container resource must be provided
        to create the resource within the provided scope

        :param data: data that will be sent to the api endpoint
        :type data: Union[list, dict], optional
        :param container_uuid: uuid of container resource
        :type container_uuid: str, optional
        :param container_name: name of container resource
        :type container_name: str, optional
        :param params: dict of parameters for http request
        :type params: dict, optional
        :return: api response
        :rtype: requests.Response
        """
        url = self.url(self.PATH.format(container_uuid=container_uuid, uuid=None))
        return self.conn.post(url, data, params, self.IGNORE_FOR_CREATE)

    @utils.resolve_by_name
    @utils.minimum_version_required
    def get(self, container_uuid=None, container_name=None, uuid=None, name=None, params=None):
        """Get api resource in json format. Either name or uuid of container resource must
        be provided to search for resources within the container scope
        If no name or uuid is provided a list of all available resources will be returned

        :param container_uuid: uuid of container resource
        :type container_uuid: str, optional
        :param container_name: name of container resource
        :type container_name: str, optional
        :param uuid: id of resource
        :type uuid: str, optional
        :param name: name of resource
        :type name: str, optional
        :param params: dict of parameters for http request
        :type params: dict, optional
        :return: api response
        :rtype: Union[dict, list]
        """
        url = self.url(self.PATH.format(container_uuid=container_uuid, uuid=uuid))
        return self.conn.get(url, params)

    @utils.resolve_by_name
    @utils.minimum_version_required
    def update(self, data: Dict, container_uuid=None, container_name=None, params=None):
        """Update existing api resource. Either name or uuid of container resource must be provided
        Existing data will be overridden with the provided payload. The request will be routed
        to the correct resource by extracting the `id` within the payload

        :param data: data that will be sent to the api endpoint
        :type data: Union[list, dict], optional
        :param container_uuid: uuid of container resource
        :type container_uuid: str, optional
        :param container_name: name of container resource
        :type container_name: str, optional
        :param params: dict of parameters for http request
        :type params: dict, optional
        :return: api response
        :rtype: requests.Response
        """
        url = self.url(self.PATH.format(container_uuid=container_uuid, uuid=data['id']))
        return self.conn.put(url, data, self.IGNORE_FOR_UPDATE)

    @utils.resolve_by_name
    @utils.minimum_version_required
    def delete(self, container_uuid=None, container_name=None, uuid=None, name=None):
        """Delete existing api resource. Either name or uuid of container resource must be provided
        Either `name` or `uuid` must be provided to delete an existing resource

        :param container_uuid: uuid of container resource
        :type container_uuid: str, optional
        :param container_name: name of container resource
        :type container_name: str, optional
        :param uuid: id of resource
        :type uuid: str, optional
        :param name: name of resource
        :type name: str, optional
        :return: api response
        :rtype: requests.Response
        """
        url = self.url(self.PATH.format(container_uuid=container_uuid, uuid=uuid))
        return self.conn.delete(url)
