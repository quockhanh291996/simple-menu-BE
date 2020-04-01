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

    add = 'add_category'
    change = 'change_category'
    delete = 'delete_category'
    view = 'view_category'
