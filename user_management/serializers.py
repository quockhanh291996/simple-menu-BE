"""
    file: user_management/serializers.py
    purpose: Define Serializer class for user model
            that help us to serialize deserialize the datatypes
"""

import logging

from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist

from user_management.constants import UserGroups

logger = logging.getLogger(__name__)


class UserSerializer(ModelSerializer):
    """ User seriazlier class """

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'groups']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])

        if not validated_data['groups'] or len(validated_data['groups']) == 0:
            # Add user to standard group by default if there are no option
            try:
                standard_group = Group.objects.get(name=UserGroups.ADMIN.value)
                standard_group.user_set.add(user)
                standard_group.save()
            except ObjectDoesNotExist:
                logger.error('Standard group doesn\'t exist!')
        else:
            for group in validated_data['groups']:
                group.user_set.add(user)
                group.save()

        return user


class UserRole(ModelSerializer):
    """ Role seriazlier class - Support for resgitration form, just for easy to demo """

    class Meta:
        model = Group
        fields = ['id', 'name']
