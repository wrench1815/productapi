from django.urls import path, include
from rest_framework import routers
# from rest_framework.routers import DefaultRouter
from .viewsets import FlipkartProductViewSet, AmazonProductViewSet

# Creates a new Router
router = routers.DefaultRouter()
router.register(r'flipkart', FlipkartProductViewSet, basename='flipkart')
router.register(r'amazon', AmazonProductViewSet, basename='amazon')
