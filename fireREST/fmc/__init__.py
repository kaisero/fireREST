# -*- coding: utf-8 -*-

import json
import logging
import re
import requests
import urllib3

from fireREST import defaults
from fireREST import exceptions as exc
from fireREST import utils

from copy import deepcopy
from http.client import responses as http_responses
from requests.auth import HTTPBasicAuth
from packaging import version
from typing import Dict, List, Union
from urllib.parse import urlencode

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Connection:

    """API Client for Firepower Management Center REST API"""

    def __init__(
        self,
        hostname: str,
        username: str,
        password: str,
        protocol=defaults.API_PROTOCOL,
        verify_cert=False,
        domain=defaults.API_DEFAULT_DOMAIN,
        timeout=defaults.API_REQUEST_TIMEOUT,
    ):
        """Initialize api client object (make sure to use a dedicated api user!)

        :param hostname: ip address or fqdn of firepower management center
        :param username: login username
        :param password: login password
        :param protocol: protocol used to access fmc rest api. Defaults to `https`
        :param verify_cert: check https certificate for validity. Defaults to `False`
        :param cache: enable result caching for get operations. Not implemented yet
        :param logger: logger instance. Defaults to `None`
        :param domain: name of the domain to access. Defaults to `Global`
        :param timeout: timeout value for http requests. Defaults to `120` seconds
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
        self.verify_cert = verify_cert
        self.domains = None
        self.login()
        self.domain = self.get_domain_id(domain)
        self.version = self.get_version()

    @utils.handle_errors
    def _request(self, method: str, url: str, params=None, auth=None, data=None):
        """base operations used for all http api calls to firepower management center

        :param method: http operations in string format (post, get, put, delete)
        :param url: url to api resource in string format
        :param params: dictionary of additional params that should be passed to the request. Defaults to `None`
        :param auth: credentials in base64 format. Defaults to `None`
        :param data: request body in dict format. Defaults to `None`
        :return: requests.response object
        """
        response = self.session.request(
            method=method,
            url=url,
            params=utils.filter_params(params),
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

        return response

    def login(self):
        """basic authentication to firepower management center rest api
        in case authentication is successful an access and refresh token are being saved to
        the `Connection` object which will be used for subsequent api calls
        """
        logger.info('Attempting authentication with Firepower Management Center (%s)', self.hostname)
        url = f'{self.protocol}://{self.hostname}{defaults.API_AUTH_URL}'
        response = self._request('post', url, auth=self.cred)
        self.headers['X-auth-access-token'] = response.headers['X-auth-access-token']
        self.headers['X-auth-refresh-token'] = response.headers['X-auth-refresh-token']
        self.domains = json.loads(response.headers['DOMAINS'])
        self.refresh_counter = defaults.API_REFRESH_COUNTER_INIT

    def refresh(self):
        """refresh authorization token. This operation is performed for up to three
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
        """Get version of fmc"""
        url = f'{self.protocol}://{self.hostname}{defaults.API_PLATFORM_URL}/info/serverversion'
        return version.parse(self._request('get', url).json()['items'][0]['serverVersion'].split(' ')[0])

    def get_domain_id(self, name: str):
        """helper function to retrieve domain id from list of domains

        :param name: name of the domain
        :return: uuid if domain is found, None otherwise
        """
        for domain in self.domains:
            if domain['name'] == name:
                return domain['uuid']
        logger.error(
            'Could not find domain with name %s. Make sure full path is provided',
            name,
        )
        available_domains = ', '.join((domain['name'] for domain in self.domains))
        logger.debug('Available Domains: %s', available_domains)
        return None


class Resource:
    """base class for api resources"""

    NAMESPACE = 'config'
    PATH = '/'
    SUPPORTED_FILTERS = []
    SUPPORTED_OPERATIONS = []

    def __init__(
        self,
        conn,
    ):
        """initialize api object (make sure to use a dedicated api user)

        :param conn: FireREST.Connection object
        """
        self._conn = conn
        self.domain = conn.domain
        self.version = conn.version

    def _url(self, path):
        """helper to generate url for requests to fmc rest api

        :return: url as string
        """
        options = {
            'base': f'{self._conn.protocol}://{self._conn.hostname}{path}',
            'config': f'{self._conn.protocol}://{self._conn.hostname}{defaults.API_CONFIG_URL}/domain/{self.domain}{path}',
            'platform': f'{self._conn.protocol}://{self._conn.hostname}{defaults.API_PLATFORM_URL}{path}',
            'refresh': f'{self._conn.protocol}://{self._conn.hostname}{defaults.API_REFRESH_URL}',
        }
        if self.NAMESPACE not in options.keys():
            raise exc.InvalidNamespaceError(f'Invalid namespace "{self.NAMESPACE}" provided. Options: {options.keys()}')
        return options[self.NAMESPACE]

    def _virtualrouter_url(self, url, virtualrouter_id=None):
        """helper that changes url to include path to virtualrouter

        :param virtualrouter_id: uuid of virtualrouter resource
        :return: adapted url that points to specified virtualrouter, same url if no virtualrouter is specified
        """
        if virtualrouter_id:
            return url.replace('/routing/', f'/routing/virtualrouters/{virtualrouter_id}/')
        return url

    @utils.handle_errors
    def _request(self, method: str, url: str, params=None, auth=None, data=None):
        """base operations used for all http api calls to firepower management center

        :param method: http operations in string format (post, get, put, delete)
        :param url: url to api resource in string format
        :param params: dictionary of additional params that should be passed to the request. Defaults to `None`
        :param auth: credentials in base64 format. Defaults to `None`
        :param data: request body in dict format. Defaults to `None`
        :return: requests.response object
        """
        response = self._conn.session.request(
            method=method,
            url=utils.fix_url(url),
            params=utils.filter_params(params),
            data=json.dumps(data),
            auth=auth,
            headers=self._conn.headers,
            timeout=self._conn.timeout,
            verify=self._conn.verify_cert,
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

        return response

    def _get(self, url: str, params=None, items=None):
        """get operation with pagination support. Returned results are automatically
        squashed in a single result

        :param url: request that should be performed
        :param params: dict of parameters for http request. Defaults to `None`
        :return: dictionary or list of returned api objects
        """
        if not utils.is_getbyid_operation(url) and items is None:
            if params is None:
                params = {}
            params['limit'] = defaults.API_PAGING_LIMIT
            params['expanded'] = defaults.API_EXPANSION_MODE

        response = self._request('get', url, params=params)
        payload = response.json()

        if 'paging' in payload:
            if items is None:
                items = []
            if 'items' in payload:
                items.extend(payload['items'])
                if 'next' in payload['paging']:
                    items = self._get(payload['paging']['next'][0], params=None, items=items)
            return items
        return payload

    def _delete(self, url: str, params=None):
        """delete operation

        :param url: request that should be performed
        :param params: dict of parameters for http request
        :return: requests.response object
        """
        return self._request('delete', url, params=params)

    def _post(self, url: str, data: Dict, params=None):
        """create operation that takes a payload as `dict` which is sent
        to the specified url to create a new resource

        :param url: request that should be performed
        :param data: dict of data that will be sent to the api
        :param params: dict of parameters for http request
        :return: requests.response object
        """
        data = self._sanitize('post', data)
        return self._request('post', url, params=params, data=data)

    def _put(self, url: str, data: Dict, params=None):
        """put operation that updates existing resources according to the payload provided

        :param url: request that should be performed
        :param json: dict of data that will be sent to the api
        :param params: dict of parameters for http request
        :return: requests.response object
        """
        data = self._sanitize('put', data)
        return self._request('put', url, data=data, params=params)

    def create(self, data: Union[dict, list], params=None):
        url = self._url(self.PATH.format(uuid=None))
        if not params:
            params = {}
        if isinstance(params, list):
            params['bulk'] = True
        return self._post(url, data, params)

    @utils.resolve_by_name
    def get(self, uuid=None, name=None, params=None):
        url = self._url(self.PATH.format(uuid=uuid))
        return self._get(url, params)

    def update(self, data: Dict):
        url = self._url(self.PATH.format(uuid=data['id']))
        return self._update(url)

    @utils.resolve_by_name
    def delete(self, uuid=None, name=None):
        url = self._url(self.PATH.format(uuid=uuid))
        return self._delete(url)


class ChildResource(Resource):
    """base class for api resources located within a container"""

    CONTAINER_NAME = 'Resource'
    CONTAINER_PATH = '/'

    def create(self, container_uuid: str, data: Union[dict, list], params=None):
        url = self._url(self.PATH.format(container_uuid=container_uuid, uuid=None))
        if not params:
            params = {}
        if isinstance(params, list):
            params['bulk'] = True
        return self._post(url, data, params)

    @utils.resolve_by_name
    def get(self, container_uuid=None, container_name=None, uuid=None, name=None, params=None):
        url = self._url(self.PATH.format(container_uuid=container_uuid, uuid=uuid))
        return self._get(url, params)

    @utils.resolve_by_name
    def update(self, data: Dict, container_uuid=None, container_name=None):
        url = self._url(self.PATH.format(container_uuid=container_uuid, uuid=data['id']))
        return self._update(url)

    @utils.resolve_by_name
    def delete(self, container_uuid=None, container_name=None, uuid=None, name=None):
        url = self._url(self.PATH.format(uuid=uuid))
        return self._delete(url)
