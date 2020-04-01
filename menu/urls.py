"""
    file: menu/urls
    purpose: Router for menu's APIs
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from menu.views import CategoryViewSet, ItemViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
