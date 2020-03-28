"""
    File: menu/constant.py
    Purpose: Define constants, enum for menu app
"""

from enum import Enum

from menu.models.category import CategoyPermission
from menu.models.item import ItemPermission


class UserGroups(Enum):
    """ Enum contains the user group for authorization in menu """

    ADMIN = 'admin_user'
    STANDARD = 'standard_user'

# Mapping object present the permissions of each user group
GROUP_PERMISSION_MAPPING = {
    UserGroups.ADMIN.value: [
        CategoyPermission.add.value,
        CategoyPermission.change.value,
        CategoyPermission.delete.value,
        CategoyPermission.view.value,
        ItemPermission.add.value,
        ItemPermission.change.value,
        ItemPermission.delete.value,
        ItemPermission.view.value,
    ],
    UserGroups.STANDARD.value: [
        CategoyPermission.view.value,
        ItemPermission.view.value,
    ]
}
