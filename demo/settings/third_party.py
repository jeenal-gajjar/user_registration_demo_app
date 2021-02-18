"""
Created:          18/02/2021
Post-History:
Title:            This module is intended to provide Django REST Framework & other 3rd parties APIs Settings.
"""

__version__ = '0.0.1'
__author__ = 'Jeenal Suthar'

from .base import *

INSTALLED_APPS += [
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'EXCEPTION_HANDLER': 'demo.utils.handler.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}

