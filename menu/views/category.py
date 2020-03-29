"""
    file: menu/views.py
    purpose: Define class-based view for apis related to menu
"""

from rest_framework.viewsets import ModelViewSet

from menu.serializers import CategorySerializer
from menu.models import Category


class CategoryViewSet(ModelViewSet):
    """ Category viewset  """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
