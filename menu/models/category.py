"""
    File: menu/model/category.py
    Purpose: Define structure for categoy of menu
"""

from enum import Enum

from django.db import models


class Category(models.Model):
    """ ORM class that present the Category table"""

    name = models.CharField(max_length=30, unique=True)


class CategoryPermission(Enum):
    """ Enum contains the permission on category model """

    app_name = 'menu'

    add = app_name + '.add_category'
    change = app_name + '.change_category'
    delete = app_name + '.delete_category'
    view = app_name + '.view_category'
