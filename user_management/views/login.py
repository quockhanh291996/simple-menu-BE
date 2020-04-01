"""
    file: login.py
    purpose: Custome the JWT view to add additional infor when get token
"""

import logging

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from user_management.serializers import UserSerializer

logger = logging.getLogger(__name__)


class LoginView(TokenObtainPairView):
    """
        Custom view to add information of user through response
    """

    @staticmethod
    def gen_payload(serializer, request):
        result = serializer.validated_data

        # Get user's information
        try:
            user = User.objects.get(username=request.data['username'])
            user_json_data = UserSerializer(user).get_info()
            result['user'] = user_json_data
        except User.DoesNotExist:
            logger.error('Authenticated user is not existed!')

        return result

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as error:
            raise InvalidToken(error.args[0])

        return Response(self.gen_payload(serializer, request), status=status.HTTP_200_OK)
