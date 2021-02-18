"""
Created:          18/02/2021
Post-History:
Title:            This module is intended to provide Database Connectivity
"""

__version__ = '0.0.1'
__author__ = 'Jeenal Suthar'

from .base import *

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

db_engine = CFG['database']['engine']
DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.{db_engine}',
        'NAME': CFG['database']['name'],
        'USER': CFG['database']['username'],
        'PASSWORD': CFG['database']['password'],
        'HOST': CFG['database']['host'],
        'PORT': CFG['database']['port'],

    }
}
