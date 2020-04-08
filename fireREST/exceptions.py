# -*- coding: utf-8 -*-


class GenericApiError(Exception):
    '''
    generic api error exception
    '''

    def __init__(self, message):
        super().__init__(message)


class InvalidNamespaceError(Exception):
    '''
    exeption thrown when invalid namespace is being passed to api
    '''

    def __init__(self, message):
        super().__init__(message)


class AuthError(Exception):
    '''
    generic api authentication failure exception
    '''

    def __init__(self, message):
        super().__init__(message)


class AuthRefreshError(Exception):
    '''
    exception used when api token refresh fails
    '''

    def __init__(self, message):
        super().__init__(message)


class RateLimitException(Exception):
    '''
    exception used when fmc rate limiter kicks in
    '''

    def __init__(self, message):
        super().__init__(message)


class UnsupportedOperationError(Exception):
    '''
    exception used when unsupported operation is being performed
    '''

    def __init__(self, message):
        super().__init__(message)


class UnsupportedObjectTypeError(Exception):
    '''
    exception used when unsupported object type is being used
    '''

    def __init__(self, message):
        super().__init__(message)
