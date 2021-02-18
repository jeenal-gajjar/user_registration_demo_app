"""
Created:          18/02/2021
Post-History:
Title:            This module is intended to provide custom exception handler.
"""

__version__ = '0.0.1'
__author__ = 'Jeenal Suthar'

from rest_framework.views import exception_handler
from rest_framework import exceptions, status
from django.http import Http404


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(exc, (exceptions.AuthenticationFailed, exceptions.NotAuthenticated)):
        response.status_code = status.HTTP_401_UNAUTHORIZED

    if response and response.status_code == status.HTTP_404_NOT_FOUND:
        raise Http404

    # Now add the HTTP status code to the response.
    if response is not None:
        data = response.data
        errors = {}
        for field, value in data.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    errors[k] = v[0] if isinstance(v, list) else v
                continue
            errors[field] = value[0] if isinstance(value, list) else value
        response.data = {'message': errors, "type": '-ERR', 'status_code': response.status_code}
    return response
