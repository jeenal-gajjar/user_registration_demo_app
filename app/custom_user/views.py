"""
Created:          18/02/2021
Post-History:
Title:            This module is intended to provide auth Apis
"""

__version__ = '0.0.1'
__author__ = 'Jeenal Suthar'

from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated

from app.custom_user.models import User
from app.custom_user.serializers import LoginSerializer, UserSerializer
from demo.utils import constants
from demo.utils.response import success_response, error_response


class LoginViewSet(viewsets.ModelViewSet):
    """ Check email and password and redirect user to dashboard page """

    permission_classes = [AllowAny, ]
    http_method_names = ['post', 'options']
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return success_response(
            constants.LOGIN_SUCCESS,
            data={
                'email': user.email,
                'dashboard_url': settings.DASHBOARD_URL
            }
        )


class LogoutViewSet(viewsets.ModelViewSet):
    """ User Logout APIView """

    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        logout(request)
        return success_response(constants.LOGOUT_SUCCESS)


class SignupViewSet(viewsets.ModelViewSet):
    """
    This class is used for User details Apis..
    """
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer
    queryset = User.objects.select_related().order_by('-id')
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
            return success_response(constants.USER_SIGNUP_SUCCESS)
        except Exception as exc:
            return error_response(constants.USER_SIGNUP_FAIL, status_code=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """ Return a User data"""

    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'patch', 'put']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        return success_response(constants.USERS_GET_SUCCESS, data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        serializer = super().retrieve(request, *args, **kwargs)
        return success_response(constants.USER_RETRIEVE_SUCCESS, data=serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = super().update(request, *args, **kwargs)
        return success_response(constants.USER_UPDATE_SUCCESS, data=serializer.data)