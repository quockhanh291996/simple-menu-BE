"""
    file: menu/permission/item.py
    purpose: Contains the custom permission for item
"""

from rest_framework import permissions

from menu.models.item import ItemPermission


class ViewItemPermission(permissions.BasePermission):
    """ Check permission to view item """

    def has_permission(self, request, view):
        return request.user.has_perm(ItemPermission.view.value)

class AddItemPermission(permissions.BasePermission):
    """ Check permission to add item """

    def has_permission(self, request, view):
        return request.user.has_perm(ItemPermission.add.value)

class UpdateItemPermission(permissions.BasePermission):
    """ Check permission to view item """

    def has_permission(self, request, view):
        return request.user.has_perm(ItemPermission.change.value)


class DeleteItemPermission(permissions.BasePermission):
    """ Check permission to view item """

    def has_permission(self, request, view):
        return request.user.has_perm(ItemPermission.delete.value)
