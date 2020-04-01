"""
    File: menu/serializer/item.py
    Purpose: Define serializer class for item of menu
"""

from rest_framework.serializers import ModelSerializer

from menu.models import Item


class ItemSerializer(ModelSerializer):
    """ Item seriazlier class """

    class Meta:
        model = Item
        fields = ['id', 'name', 'category', 'description', 'thumbnail_image']
