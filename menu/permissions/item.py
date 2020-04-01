"""
    file: menu/permission/item.py
    purpose: Contains the custom permission for item
"""

from rest_framework import permissions

from menu.models.item import ItemPermission


app_name = ItemPermission.app_name.value

class ViewItemPermission(permissions.BasePermission):
    """ Check permission to view item """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, ItemPermission.view.value))

class AddItemPermission(permissions.BasePermission):
    """ Check permission to add item """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, ItemPermission.add.value))

class UpdateItemPermission(permissions.BasePermission):
    """ Check permission to view item """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, ItemPermission.change.value))


class DeleteItemPermission(permissions.BasePermission):
    """ Check permission to view item """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, ItemPermission.delete.value))
