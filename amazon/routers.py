from django.urls import path, include
from rest_framework import routers

from amazon import viewsets

# Creates a new Router
router = routers.DefaultRouter()
router.register(r'product',
                viewsets.AmazonProductViewSet,
                basename='amamzonProduct')
router.register(r'brand', viewsets.AmazonBrandViewSet, basename='amamzonBrand')
router.register(r'category',
                viewsets.AmazonCategoryViewSet,
                basename='amamzonCategory')
router.register(r'vendor',
                viewsets.AmazonVendorViewSet,
                basename='amamzonVendor')
