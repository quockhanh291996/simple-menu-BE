"""
    file: user_management/models
    purpose: Use the User model of djang-auth app,
            but will define the permission enum on user table here
"""
from enum import Enum

class UserPermission(Enum):
    """ Enum contains the permission on user model """

    # Name of app cotain user model
    app_name = 'auth'

    add = 'add_user'
    change = 'change_user'
    delete = 'delete_user'
    view = 'view_user'
