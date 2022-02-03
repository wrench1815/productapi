from rest_framework import viewsets

from .models import Product, Category, Brand, Vendor
from flipkart import serializers


class FlipkartProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.FlipkartProductSerializer


class FlipkartCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.FlipkartCategorySerializer


class FlipkartBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = serializers.FlipkartBrandSerializer


class FlipkartVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = serializers.FlipkartVendorSerializer
