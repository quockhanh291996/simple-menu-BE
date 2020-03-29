"""
    File: menu/serializer/category.py
    Purpose: Define serializer class for categoy of menu
"""

from rest_framework.serializers import ModelSerializer

from menu.models import Category


class CategorySerializer(ModelSerializer):
    """ Category seriazlier class """

    class Meta:
        model = Category
        fields = ['id', 'name']
