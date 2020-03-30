"""
    file: account/views/role.py
    purpose: Define class-based view for apis related to account
"""

from rest_framework.viewsets import ReadOnlyModelViewSet

from django.contrib.auth.models import Group

from user_management.serializers import UserRole


class UserRoleSet(ReadOnlyModelViewSet):
    """ Role viewset class - Just read-only to FE get the role when resgister"""

    queryset = Group.objects.all()
    serializer_class = UserRole
