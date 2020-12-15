import re
import sys

from copy import deepcopy
from http.client import responses as http_responses
from functools import lru_cache, wraps
from logging import getLogger
from requests.exceptions import HTTPError
from retry import retry
from packaging import version
from time import sleep
from typing import Dict
from uuid import UUID, uuid4

from . import exceptions as exc
from .mapping import FILTERS, PARAMS, OBJECT_TYPE

logger = getLogger(__name__)


def is_uuid(val: str):
    """
    verify if a value is valid uuid
    : param val: unique identifier in string format
    : return: True if valid uuid, False if invalid uuid
    """
    try:
        UUID(val)
        return True
    except ValueError:
        return False


def is_getbyid_operation(url: str):
    """
    verify if a api call is to a specific resource or a list of resources
    : param url: request in str format
    : return: True if resource is queried, False if multiple resources are being queried
    """
    uuid = url.split('?')[0].split('/')[-1]
    if is_uuid(uuid):
        return True
    return False


def cache_result(f):
    """
    decorator that applies functools lru_cache if cache is enabled in Client object
    """

    def inner_function(f):
        @lru_cache(maxsize=256)
        def cache(*args, **kwargs):
            return f(*args, **kwargs)

        @wraps(f)
        @lru_cache(maxsize=256)
        def wrapper(*args, **kwargs):
            if args[0].cache is True:
                return cache
            return f(*args, **kwargs)

        return wrapper

    return inner_function


def log_request(action):
    """
    decorator that adds additional debug logging for api requests
    """

    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            logger = args[0].logger
            request = args[1]
            request_id = str(uuid4())[:8]
            try:
                data = args[3]
            except IndexError:
                data = None
            logger.debug('[%s] [%s] %s', request_id, action, request)
            if data:
                logger.debug('[%s] [Data] %s', request_id, data)
            result = f(*args)
            status_code = result.status_code
            status_code_name = http_responses[status_code]
            logger.debug('[%s] [Response] %s (%s)', request_id, status_code_name, status_code)
            if status_code >= 299:
                logger.debug('[%s] [Message] %s', request_id, result.content)
            return result

        return wrapper

    return inner_function


def minimum_version_required(minimum_version):
    """
    decorator that specifies the minimal required software version to use the operation
    """
    minimum_version = version.parse(minimum_version)

    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                installed_version = args[0].version
            except AttributeError:
                return f(*args, **kwargs)
            if installed_version < minimum_version:
                raise exc.UnsupportedOperationError(
                    f'{f.__name__} requires fmc software version {minimum_version}. Installed version: {installed_version}',
                )
            return f(*args, **kwargs)

        return wrapper

    return inner_function


def validate_object_type(f):
    """
    decorator that validates object type and transforms input if neccessary
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            object_type = kwargs.get('object_type', None)
            if object_type:
                kwargs['object_type'] = OBJECT_TYPE[object_type.lower()]
            else:
                args = list(args)
                object_type = args[1]
                args[1] = OBJECT_TYPE[object_type.lower()]
        except KeyError:
            if object_type in OBJECT_TYPE.values():
                return f(*args, **kwargs)
            raise exc.UnsupportedObjectTypeError(f'{object_type} is not a valid object type')
        return f(*args, **kwargs)

    return wrapper


def resolve_by_name(f):
    """decorator that adds support for resolving resource via name"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        resource = args[0]
        container_name = kwargs.get('container_name', None)
        container_uuid = kwargs.get('container_uuid', None)
        name = kwargs.get('name', None)
        uuid = kwargs.get('uuid', None)

        if container_name and not container_uuid:
            url = resource._url(resource.CONTAINER_PATH.format(uuid=None))
            for item in resource._get(url):
                if item['name'] == container_name:
                    kwargs['container_uuid'] = item['id']
                    break
            else:
                raise exc.ResourceNotFoundError(
                    msg=f'Resource of type {resource.CONTAINER_PATH} with name "{resource.CONTAINER_NAME}" does not exist'
                )
        if name and not uuid and name not in resource.SUPPORTED_FILTERS:
            for item in resource.get.__wrapped__(*args, **kwargs):
                if item['name'] == name:
                    if f.__name__ == 'get':
                        kwargs['result'] = item
                    else:
                        kwargs['uuid'] = item['id']
                    break
            else:
                raise exc.ResourceNotFoundError(
                    msg=f'Resource of type {resource.__class__.__name__} with name "{name}" does not exist'
                )
        if 'result' in kwargs:
            return kwargs['result']
        return f(*args, **kwargs)

    return wrapper


def support_params(f):
    """decorator that adds support for resolving resources by using filter params"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        resource = args[0]
        data = kwargs.get('data', None)
        filters = []
        params = {}

        # if payload is of type list the bulk param should be set automatically
        if isinstance(data, list):
            params['bulk'] = True

        # search through function kwargs to locate filter and param arguments
        for k, v in kwargs.items():
            if v:
                if k in resource.SUPPORTED_FILTERS:
                    filters.append({FILTERS[k]: v})
                elif k in resource.SUPPORTED_PARAMS:
                    params[PARAMS[k]] = v
        params['filter'] = search_filter(filters)
        kwargs['params'] = {**kwargs['params'], **params} if kwargs['params'] else params
        return f(*args, **kwargs)

    return wrapper


def handle_errors(f):
    """decorator that handles common api errors automatically"""

    @wraps(f)
    @retry(exceptions=exc.RateLimitException, tries=6, delay=10, logger=logger)
    def wrapper(*args, **kwargs):
        fmc = args[0]
        try:
            validate_data(kwargs.get('method', args[1]), kwargs.get('data', args[-1]))
            response = f(*args, **kwargs)
            response.raise_for_status()
        except HTTPError:
            if response.status_code == 401 and 'Access token invalid' in response.text:
                # Invalid access token detected. Refresh authorization token
                fmc.conn.refresh()
            else:
                raise_for_status(response)
        return response

    return wrapper


def validate_data(method, data):
    """
    validate payload that will be sent to fmc for errors
    """
    if method != 'get':
        if sys.getsizeof(data) > 2048000:
            raise exc.PayloadLimitExceededError


def raise_for_status(response):
    """
    raise exception based on error received by fmc
    """
    status_code = response.status_code
    exceptions = {
        400: exc.GenericApiError,
        404: exc.ResourceNotFoundError,
        422: exc.UnprocessableEntityError,
        429: exc.RateLimitException,
        500: exc.GenericApiError,
    }
    errors = {
        400: [{'msg': 'Duplicate Name', 'exception': exc.ResourceAlreadyExistsError}],
        401: [{'msg': 'User authentication failed', 'exception': exc.AuthError}],
    }
    if status_code in errors:
        for error in errors[status_code]:
            if error['msg'] in response.text:
                raise error['exception'](msg=response.json()['error']['messages'][0]['description'])
    try:
        raise exceptions.get(status_code, HTTPError)(msg=response.json()['error']['messages'][0]['description'])
    except ValueError:
        raise exceptions.get(status_code, HTTPError)()


def search_filter(items=None):
    """helper that generates a filter string from a list of key,value pairs

    :param items: list of key value pairs in dict format used to build filter string
    :return: valid filter string or an empty filter string if items passed are invalid
    """
    if items:
        filter_str = ''
        for k, v in items.items():
            if v:
                filter_str += f'{k}:{v};'
        return filter_str.rstrip(';')
    return ''


def filter_params(params: Dict):
    """helper that filters out params with empty values

    :param params: request params in dict format
    :return: new params dictionary that only includes valid entries or an empty dict if params was empty
    """
    if isinstance(params, dict):
        return {k: v for k, v in params.items() if v is not None and v != ''}
    return {}


def fix_url(url: str):
    """helper that fixed api calls that end with '/' or '/None'

    :param url: request url in str format
    :return: fixed url
    """
    return re.sub(r'\/None$', '', url).rstrip('/')


def sanitize_payload(method: str, payload: Dict, ignore_fields=None, recursive=False):
    """sanitize json object for api operation
    This is neccesarry since fmc api cannot handle json objects with some
    fields that are received via get operations (e.g. link, metadata). The provided
    payload will be copied to ensure the provided data is not manipulated by `_sanitize`

    :param payload: api object in dict format
    :return: sanitized api object in dict format
    """
    if not recursive:
        payload = deepcopy(payload)
    if not isinstance(payload, list):
        payload.pop('metadata', None)
        payload.pop('links', None)
        for item in ignore_fields:
            payload.pop(item, None)
        if method.lower() == 'post':
            payload.pop('id', None)
    else:
        for item in payload:
            item = sanitize_payload(method, item, ignore_fields, recursive=True)
    return payload
