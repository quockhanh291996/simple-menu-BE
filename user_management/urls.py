"""
    file: user_management/urls
    purpose: Router for account's APIs
"""
from django.contrib import admin
from django.urls import path

from rest_framework import renderers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_management.views import UserViewSet, UserRoleSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', UserRoleSet)

urlpatterns = [
    path('', include(router.urls)),
]