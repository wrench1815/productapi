from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet as fProductViewSet

# Creates a new Router
router = DefaultRouter()
router.register(r'products', fProductViewSet)
