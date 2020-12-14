# -*- coding: utf-8 -*-

from . import defaults


class GenericApiError(Exception):
    """generic api error"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidNamespaceError(Exception):
    """invalid namespace is being passed"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class AuthError(Exception):
    """generic authentication failure"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class AuthRefreshError(Exception):
    """api token refresh cannot be refreshed"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class RateLimitException(Exception):
    """fmc rate limiter kicks in"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnsupportedOperationError(Exception):
    """unsupported operation is being performed"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnsupportedObjectTypeError(Exception):
    """unsupported object type is being used"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnprocessableEntityError(Exception):
    """unprocessable entity passed to fmc rest api"""

    MSG = (
        'The payload contains an unprocessable or unreadable entity'
        'such as a invalid attribute name or incorrect JSON syntax'
    )

    def __init__(self, msg=MSG, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class PayloadLimitExceededError(Exception):
    """size limit of api payload is exceeded"""

    MSG = f'Payload exceeds maximum size of {defaults.API_PAYLOAD_SIZE_MAX}'

    def __init__(self, msg=MSG, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class ResourceNotFoundError(Exception):
    """requested resource cannot not be found"""

    def __init__(self, msg, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
