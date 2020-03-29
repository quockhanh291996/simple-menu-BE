"""
    File: menu/model/item.py
    Purpose: Define structure for item in menu
"""

from enum import Enum

from django.db import models

from .category import Category


class Item(models.Model):
    """ ORM class that present the Category table"""

    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=120)
    thumbnail_image = models.ImageField(upload_to='uploads/%Y/%m')


class ItemPermission(Enum):
    """ Enum contains the permission on item model """

    app_name = 'menu'

    add = app_name + '.add_item'
    change = app_name + '.change_item'
    delete = app_name + '.delete_item'
    view = app_name + '.view_item'
