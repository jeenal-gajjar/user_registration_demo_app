"""
Created:          18/02/2021
Post-History:
Title:            This module is intended to provide auth APIs Serializers.
"""

__version__ = '0.0.1'
__author__ = 'Jeenal Suthar'

import re

from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from app.custom_user.models import User


def password_validator(password):
    """
    This function validate Password with a minimum 8 digits with 1 Symbol, 1 Capital Letter, and 1 Number
    :param password:
    :return:
    """
    reg = "^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&/]{8,}$"
    pattern = re.compile(reg)
    if not re.search(pattern, password):
        raise ValidationError(
            _("Please enter a password with a minimum 8 digits with 1 Symbol, 1 Capital Letter, and 1 Number."),
            code='password_no_number',
        )
    return password


class LoginSerializer(serializers.ModelSerializer):
    """
    This class is used to hold User Serializer Information.
    """
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        user = None
        email = attrs.get('email', None)
        password = attrs.get('password', None)

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)
            if not user:
                raise AuthenticationFailed()

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    """
    This class is used to hold User Serializer Information.
    """
    password = serializers.CharField(max_length=20, min_length=8, write_only=True, validators=[password_validator])

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['is_superuser']:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
