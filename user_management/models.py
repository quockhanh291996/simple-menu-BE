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

    add = app_name + '.add_user'
    change = app_name + '.change_user'
    delete = app_name + '.delete_user'
    view = app_name + '.view_user'
