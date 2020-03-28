"""
    File: category.py
    Purpose: Define structure for categoy of menu
"""

from django.db import models

class Category(models.Model):
    """ ORM class that present the Category table"""

    name = models.CharField(max_length=30)
