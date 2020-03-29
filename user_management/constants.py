"""
    File: account/constant.py
    Purpose: Define constants, enum for account app
"""

from enum import Enum

from user_management.models import UserPermission

class UserGroups(Enum):
    """ Enum contains the user group for authorization in menu """

    ADMIN = 'admin_user'
    STANDARD = 'standard_user'


USER_PERSMISSION_MAPPING = {
    UserGroups.ADMIN.value: [
        UserPermission.add.value,
        UserPermission.change.value,
        UserPermission.delete.value,
        UserPermission.view.value,
    ],
    UserGroups.STANDARD.value: [
        UserPermission.add.value,
    ]
}
