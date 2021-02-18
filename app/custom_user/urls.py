"""
Created:          18/02/2021
Post-History:
Title:            This module is intended to provide bm Urls.
"""

__version__ = '0.0.1'
__author__ = 'Jeenal Suthar'

from django.shortcuts import redirect

from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'login', LoginViewSet, basename="login")
router.register(r'logout', LogoutViewSet, basename="logout")
router.register(r'signup', SignupViewSet, basename="signup")
router.register(r'user', UserViewSet, basename="user")

urlpatterns = [
    path('', lambda x: redirect('/login/')),
    path('', include(router.urls)),
]