from django.urls import path, include
from rest_framework import routers

from . import viewsets

# Creates a new Router
router = routers.DefaultRouter()
router.register(r'mobile',
                viewsets.AmazonMobileViewSet,
                basename='amazonMobile')
router.register(r'brand', viewsets.AmazonBrandViewSet, basename='amazonBrand')
router.register(r'vendor',
                viewsets.AmazonVendorViewSet,
                basename='amazonVendor')
