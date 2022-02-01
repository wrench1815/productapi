from rest_framework import viewsets

from .models import Product, Category, Brand, Vendor
from amazon import serializers


class AmazonProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.AmazonProductSerializer


class AmazonCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.AmazonCategorySerializer


class AmazonBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = serializers.AmazonBrandSerializer


class AmazonVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = serializers.AmazonVendorSerializer
