"""
    file: menu/permission/category.py
    purpose: Contains the custom permission for category
"""

from rest_framework import permissions

from menu.models.category import CategoryPermission


app_name = CategoryPermission.app_name.value

class ViewCategoryPermission(permissions.BasePermission):
    """ Check permission to view category """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, CategoryPermission.view.value))

class AddCategoryPermission(permissions.BasePermission):
    """ Check permission to add category """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, CategoryPermission.add.value))

class UpdateCategoryPermission(permissions.BasePermission):
    """ Check permission to view category """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, CategoryPermission.change.value))


class DeleteCategoryPermission(permissions.BasePermission):
    """ Check permission to view category """

    def has_permission(self, request, view):
        return request.user.has_perm(('%s.%s') % (app_name, CategoryPermission.delete.value))
