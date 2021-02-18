"""
Created:          18/02/2021
Post-History:
Title:            This module is intended to provide custom Response.
"""

__version__ = '0.0.1'
__author__ = 'Jeenal Suthar'

from rest_framework import status
from rest_framework.response import Response


def success_response(message, data=None):
    """
    This Function is used to return Custom Success Response
    :param message:
    :param data:
    :return:
    """
    response = {"message": message, "type": "+OK", "status_code": status.HTTP_200_OK, "headers": "Success"}
    if data:
        response["data"] = data
    return Response(response, status=status.HTTP_200_OK)


def error_response(message, errors=None, status_code=status.HTTP_202_ACCEPTED):
    """
    This Function is used to return Custom Error Response
    :param message:
    :param errors:
    :param status_code:
    :return:
    """
    response = {"message": message, "status_code": status_code, "type": "-ERR"}
    if errors:
        response["errors"] = errors
    return Response(response, status=status_code)