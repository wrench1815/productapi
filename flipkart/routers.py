from django.urls import path, include
from rest_framework import routers

from flipkart import viewsets

# Creates a new Router
router = routers.DefaultRouter()
router.register(r'product',
                viewsets.FlipkartProductViewSet,
                basename='flipkartProduct')
router.register(r'brand',
                viewsets.FlipkartBrandViewSet,
                basename='flipkartBrand')
router.register(r'category',
                viewsets.FlipkartCategoryViewSet,
                basename='flipkartCategory')
router.register(r'vendor',
                viewsets.FlipkartVendorViewSet,
                basename='flipkartVendor')
