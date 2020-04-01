"""
    file: menu/views/category.py
    purpose: Define class-based view for apis related to menu
"""

from rest_framework.viewsets import ModelViewSet

from menu.serializers import CategorySerializer
from menu.models import Category
from menu.permissions import (
    ViewCategoryPermission,
    AddCategoryPermission,
    UpdateCategoryPermission,
    DeleteCategoryPermission
)


class CategoryViewSet(ModelViewSet):
    """ Category viewset  """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        """
            Function to get permission on API

            # Note: Instead just check Admin, I create specific permission
              If we have many group later, we can just change the code of permission,
              don't need change the view too much
        """
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [ViewCategoryPermission,]
        elif self.action in ['create']:
            self.permission_classes = [AddCategoryPermission]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [UpdateCategoryPermission]
        elif self.action in ['destroy']:
            self.permission_classes = [DeleteCategoryPermission]

        return [permission() for permission in self.permission_classes]
