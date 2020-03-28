"""
    File: item.py
    Purpose: Define structure for item in menu
"""

from django.db import models

from .category import Category

class Item(models.Model):
    """ ORM class that present the Category table"""

    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=120)
    thumbnail_image = models.ImageField(upload_to='uploads/%Y/%m')
