from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serializers


class CustomResultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class FlipkartMobileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Mobile.objects.all()
    serializer_class = serializers.FlipkartMobileSerializer
    pagination_class = CustomResultPagination


class FlipkartBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.FlipkartBrandSerializer


class FlipkartVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.FlipkartVendorSerializer
