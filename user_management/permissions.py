"""
    file: user_management/permissions.py
    purpose: Contains the custom permission for user
"""

from rest_framework import permissions

from user_management.models import UserPermission


app_name = UserPermission.app_name.value

class ViewUserPermission(permissions.BasePermission):
    """ Check permission to view user """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, UserPermission.view.value))


class UpdateUserPermission(permissions.BasePermission):
    """ Check permission to view user """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, UserPermission.change.value))


class DeleteUserPermission(permissions.BasePermission):
    """ Check permission to view user """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, UserPermission.delete.value))
