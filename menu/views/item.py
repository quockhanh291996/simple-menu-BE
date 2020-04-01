"""
    file: menu/view/item.py
    purpose: Define class-based view for apis related to menu
"""

from rest_framework.viewsets import ModelViewSet

from menu.serializers import ItemSerializer
from menu.models import Item
from menu.permissions import (
    ViewItemPermission,
    AddItemPermission,
    UpdateItemPermission,
    DeleteItemPermission
)


class ItemViewSet(ModelViewSet):
    """ Item viewset  """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        category_id = self.request.query_params.get('categoryID', None)
        if category_id is not None:
            queryset = queryset.filter(category__pk=category_id)
        return queryset

    def get_permissions(self):
        """
            Function to get permission on API

            # Note: Instead just check Admin, I create specific permission
              If we have many group later, we can just change the code of permission,
              don't need change the view too much
        """
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [ViewItemPermission,]
        elif self.action in ['create']:
            self.permission_classes = [AddItemPermission]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [UpdateItemPermission]
        elif self.action in ['destroy']:
            self.permission_classes = [DeleteItemPermission]

        return [permission() for permission in self.permission_classes]
