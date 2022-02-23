from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serializers


class CustomResultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AmazonMobileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Mobile.objects.all()
    serializer_class = serializers.AmazonMobileSerializer
    pagination_class = CustomResultPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price']
    ordering = ['-id']


class AmazonBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.AmazonBrandSerializer


class AmazonVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.AmazonVendorSerializer
