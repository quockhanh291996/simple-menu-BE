"""
    file: account/views.py
    purpose: Define class-based view for apis related to account
"""

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from django.contrib.auth.models import User, Group

from user_management.serializers import UserSerializer, UserRole
from user_management import permissions


class UserViewSet(ModelViewSet):
    """ User viewset  """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
            Function to get permission on API

            # Note: Instead just check Admin, I create specific permission
              If we have many group later, we can just change the code of permission,
              don't need change the view too much
        """
        if self.action in ['retrieve','list']:
            self.permission_classes = [permissions.ViewUserPermission,]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [permissions.UpdateUserPermission]
        elif self.action in ['destroy']:
            self.permission_classes = [permissions.UpdateUserPermission]

        return [permission() for permission in self.permission_classes]


class UserRoleSet(ReadOnlyModelViewSet):
    """ Role viewset class - Just read-only to FE get the role when resgister"""

    queryset = Group.objects.all()
    serializer_class = UserRole
