"""
    file: menu/urls
    purpose: Router for menu's APIs
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from menu.views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
