"""
    File: account/constant.py
    Purpose: Define constants, enum for account app
"""

from enum import Enum

from menu.models.category import CategoyPermission
from menu.models.item import ItemPermission


class UserGroups(Enum):
    """ Enum contains the user group for authorization in menu """

    ADMIN = 'admin_user'
    STANDARD = 'standard_user'
