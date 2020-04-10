# -*- coding: utf-8 -*-

from . import defaults


class GenericApiError(Exception):
    '''
    generic api error exception
    '''

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidNamespaceError(Exception):
    '''
    exeption thrown when invalid namespace is being passed to api
    '''

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class AuthError(Exception):
    '''
    generic api authentication failure exception
    '''

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class AuthRefreshError(Exception):
    '''
    exception used when api token refresh fails
    '''

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class RateLimitException(Exception):
    '''
    exception used when fmc rate limiter kicks in
    '''

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnsupportedOperationError(Exception):
    '''
    exception used when unsupported operation is being performed
    '''

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnsupportedObjectTypeError(Exception):
    '''
    exception used when unsupported object type is being used
    '''

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnprocessableEntityError(Exception):
    '''
    exception used when unprocessable entity was passed to api call
    '''

    MSG = 'The payload contains an unprocessable or unreadable entity' \
          'such as a invalid attribut name or incorrect JSON syntax'

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class PayloadLimitExceededError(Exception):
    '''
    exception used when size limit of api payload is exceeded
    '''
    MSG = f'Payload exceeds maximum size of {defaults.API_PAYLOAD_SIZE_MAX}'

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
