"""
    file: user_management/urls
    purpose: Router for account's APIs
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt import views as jwt_views

from user_management.views import UserViewSet, UserRoleSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', UserRoleSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='get_token'),
]
