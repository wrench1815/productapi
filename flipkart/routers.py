from django.urls import path, include
from rest_framework import routers

from . import viewsets

# Creates a new Router
router = routers.DefaultRouter()
router.register(r'mobile',
                viewsets.FlipkartMobileViewSet,
                basename='flipkartMobile')
router.register(r'brand',
                viewsets.FlipkartBrandViewSet,
                basename='flipkartBrand')
router.register(r'vendor',
                viewsets.FlipkartVendorViewSet,
                basename='flipkartVendor')
