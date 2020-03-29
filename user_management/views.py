"""
    file: account/views.py
    purpose: Define class-based view for apis related to account
"""

from rest_framework import viewsets

from django.contrib.auth.models import User, Group

from user_management.serializers import UserSerializer, UserRole


class UserViewSet(viewsets.ModelViewSet):
    """ User viewset  """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRoleSet(viewsets.ReadOnlyModelViewSet):
    """ Role viewset class - Just read-only to FE get the role when resgister"""

    queryset = Group.objects.all()
    serializer_class = UserRole
