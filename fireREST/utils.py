import re
import sys
from copy import deepcopy
from functools import wraps
from logging import getLogger
from typing import Dict
from uuid import UUID

import packaging
from requests.exceptions import HTTPError
from retry import retry

from . import exceptions as exc
from .mapping import FILTERS, PARAMS

logger = getLogger(__name__)


def is_uuid(val: str):
    """verify if a value is valid uuid

    :param val: unique identifier in string format
    :type val: str
    :return: True if valid uuid, False if invalid uuid
    :rtype: bool
    """
    try:
        UUID(val)
        return True
    except ValueError:
        return False


def is_getbyid_operation(url: str):
    """verify if a api call is to a specific resource or a list of resources

    :param url: path to api resource
    :type url: str
    :return: True if resource is queried, False if multiple resources are being queried
    :rtype: bool
    """
    uuid = url.split('?')[0].split('/')[-1]
    if is_uuid(uuid):
        return True
    return False


def minimum_version_required(func=None, version=None):
    """Verify if operation is supported by fmc

    decorator that verifies if the called operation is supported by `Resource`. If the minimum
    version required specified in `Resource` is >= the installed FMC software version the operation
    will be performed.

    :raise  UnsupportedOperationError: if operation is not supported by FMC
    """

    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if version:
                min_version = packaging.version.parse(version)
            else:
                operations = {
                    'create': args[0].MINIMUM_VERSION_REQUIRED_CREATE,
                    'get': args[0].MINIMUM_VERSION_REQUIRED_GET,
                    'update': args[0].MINIMUM_VERSION_REQUIRED_UPDATE,
                    'delete': args[0].MINIMUM_VERSION_REQUIRED_DELETE,
                }
                min_version = packaging.version.parse(operations[f.__name__])

            installed_version = args[0].version
            if installed_version < min_version:
                raise exc.UnsupportedOperationError(
                    f'{f.__name__} operation for resource {args[0].__class__.__name__} is not supported on Firepower '
                    f'Management Center version {installed_version}',
                )
            return f(*args, **kwargs)

        return wrapper

    if func:
        return inner_function(func)
    return inner_function


def resolve_by_name(f):
    """Resolve `container_name` or `name` of `Resource` to uuid

    decorator that adds support for resolving resource uuid via name
    `resolve_by_name` checks if operations are performed with names instead of uuids and depending
    on the resource will try to find the uuid by searching for the name by iterating over all available items. In
    case a resource supports filter options or filter params it will query fmc api using the available filters
    :raise ResourceNotFoundError: if a resource or parent resource cannot be found by name
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        resource = args[0]
        container_name = kwargs.get('container_name', None)
        container_uuid = kwargs.get('container_uuid', None)
        name = kwargs.get('name', None)
        uuid = kwargs.get('uuid', None)
        params = deepcopy(kwargs.get('params', None))

        if container_name and not container_uuid:
            url = resource.url(resource.CONTAINER_PATH.format(uuid=None))
            for item in resource.conn.get(url=url, params=None):
                if item['name'] == container_name:
                    container_uuid = item['id']
                    kwargs['container_uuid'] = container_uuid
                    break
            else:
                raise exc.ResourceNotFoundError(
                    msg=f'Resource of type {resource.CONTAINER_NAME} with name "{container_name}" does not exist'
                )

        if name and not uuid:
            url = resource.url(resource.PATH.format(container_uuid=container_uuid, uuid=None))
            for item in resource.conn.get(url=url, params=params):
                if item['name'] == name:
                    if f.__name__ == 'get':
                        kwargs['result'] = item
                    else:
                        kwargs['uuid'] = item['id']
                        # Make sure name param is not passed to !GET api request
                        kwargs['name'] = None
                    break
            else:
                raise exc.ResourceNotFoundError(
                    msg=f'Resource of type {resource.__class__.__name__} with name "{name}" does not exist'
                )
        if 'result' in kwargs.keys():
            return kwargs['result']
        return f(*args, **kwargs)

    return wrapper


def support_params(f):
    """Apply `Resource` specific params to api operation

    decorator that adds support for specified filter or params options. If a list is passed
    in PUT or POST operations the `bulk` param is automatically set. Available filters and params
    are checked against `Resource.SUPPORTED_FILTERS` and `Resource.SUPPORTED_PARAMS`. If a match is found
    params are set accordingly and passed to the operations implementation
    """

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
        kwargs['params'] = {**kwargs['params'], **params} if 'params' in kwargs else params
        return f(*args, **kwargs)

    return wrapper


def handle_errors(f):
    """Exception handler for api requests

    decorator that handles common api errors automatically by checking both status codes and error messages
    within requests

    """

    @wraps(f)
    @retry(exceptions=exc.RateLimitException, tries=6, delay=10, logger=logger)
    def wrapper(*args, **kwargs):
        fmc = args[0]
        try:
            validate_data(kwargs.get('method', args[1]), kwargs.get('data', args[-1]))
            response = f(*args, **kwargs)
            # only applicable if dry_run is disabled
            if not args[0].dry_run:
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
    """Validate api payload

    Validate payload that will be sent to fmc for errors

    :raise PayloadLimitExceededError: if payload is larger than max supported payload size

    ..todo:: add support for checking payload against data model
    """
    if method != 'get':
        if sys.getsizeof(data) > 2048000:
            raise exc.PayloadLimitExceededError


def raise_for_status(response):
    """raise exception based on error received by fmc

    :param response: api response from FMC
    :type response: requests.Response
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
        400: [
            {'msg': 'Duplicate Name', 'exception': exc.ResourceAlreadyExistsError},
            {'msg': 'You do not have the required authorization', 'exception': exc.AuthorizationError},
        ],
        401: [{'msg': 'User authentication failed', 'exception': exc.AuthError}],
        403: [{'msg': 'The user is not authorized', 'exception': exc.AuthorizationError}],
        405: [{'msg': 'is not supported', 'exception': exc.UnsupportedOperationError}],
    }
    if status_code in errors:
        for error in errors[status_code]:
            if error['msg'] in response.text:
                raise error['exception'](msg=response.json()['error']['messages'][0]['description'])
    try:
        raise exceptions.get(status_code, exc.GenericApiError)(
            msg=response.json()['error']['messages'][0]['description']
        )
    except ValueError:
        raise exceptions.get(status_code, HTTPError)()


def search_filter(items=None):
    """generates a filter string from a list of key,value pairs

    :param items: list of key value pairs in dict format used to build filter string
    :type items: list, optional
    :return: valid filter string or an empty filter string if items passed are invalid
    :rtype: str
    """
    if items:
        filter_str = ''
        for item in items:
            for k, v in item.items():
                if v:
                    filter_str += f'{k}:{v};'
        return filter_str.rstrip(';')
    return ''


def fix_params(params: Dict):
    """filter out params with empty values

    :param params: request params
    :type params: dict, optional
    :return: new params dictionary that only includes valid entries or an empty dict if params was empty
    """
    if isinstance(params, dict):
        return {k: v for k, v in params.items() if v is not None and v != ''}
    return {}


def fix_url(url: str):
    """fix api calls that end with '/' or '/None'

    :param url: request url
    :type url: str
    :return: fixed url
    :rtype: str
    """
    return re.sub(r'/None$', '', url).rstrip('/')


def sanitize_payload(method: str, payload: Dict, ignore_fields=None, _recursive=False):
    """sanitize json object for api operation

    Sanitize json object for api operation. This is necessary since fmc api cannot handle json objects with some
    fields that are received via get operations (e.g. link, metadata). The provided
    payload will be copied to ensure the provided data is not manipulated

    :param method: api operation. Options: ['post', 'put', 'get']
    :type method: str
    :param payload: api object in dict format
    :param ignore_fields: fields that should be popped
    :type ignore_fields: list, optional
    :param _recursive: specifies if `sanitize_payload` is called by itself. Only called by function itself
    :type _recursive: bool
    :return: sanitized api object
    :rtype: Union[dict, list]
    """
    if not _recursive:
        payload = deepcopy(payload)
    if not isinstance(payload, list):
        payload.pop('metadata', None)
        payload.pop('links', None)
        if ignore_fields:
            for item in ignore_fields:
                payload.pop(item, None)
        if method.lower() == 'post':
            payload.pop('id', None)
    else:
        for item in payload:
            sanitize_payload(method, item, ignore_fields, _recursive=True)
    return payload
