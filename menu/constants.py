"""
    File: menu/constant.py
    Purpose: Define constants, enum for menu app
"""

from user_management.constants import UserGroups

from menu.models.category import CategoryPermission
from menu.models.item import ItemPermission

# Mapping object present the permissions of each user group
GROUP_PERMISSION_MAPPING = {
    UserGroups.ADMIN.value: [
        CategoryPermission.add.value,
        CategoryPermission.change.value,
        CategoryPermission.delete.value,
        CategoryPermission.view.value,
        ItemPermission.add.value,
        ItemPermission.change.value,
        ItemPermission.delete.value,
        ItemPermission.view.value,
    ],
    UserGroups.STANDARD.value: [
        CategoryPermission.view.value,
        ItemPermission.view.value,
    ]
}
