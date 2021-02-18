"""
Created:          18/02/2021
Post-History:
Title:            This module is intended to provide Admin Interface.
"""

__version__ = '0.0.1'
__author__ = 'Jeenal Suthar'

from app.custom_user.models import User

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


class EmailUserAdmin(UserAdmin):
    """EmailUser Admin model."""
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
                         None, {
                             'classes': ('wide',),
                             'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')
                         }
                     ),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, EmailUserAdmin)

