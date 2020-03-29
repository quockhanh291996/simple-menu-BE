"""
    file: user_management/permissions.py
    purpose: Contains the custom permission for user
"""

from rest_framework import permissions

from user_management.models import UserPermission


class ViewUserPermission(permissions.BasePermission):
    """ Check permission to view user """

    def has_permission(self, request, view):
        return request.user.has_perm(UserPermission.view.value)


class UpdateUserPermission(permissions.BasePermission):
    """ Check permission to view user """

    def has_permission(self, request, view):
        return request.user.has_perm(UserPermission.change.value)


class DeleteUserPermission(permissions.BasePermission):
    """ Check permission to view user """

    def has_permission(self, request, view):
        return request.user.has_perm(UserPermission.delete.value)
