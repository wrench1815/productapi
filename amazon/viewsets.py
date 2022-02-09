from rest_framework import viewsets

from . import models
from . import serializers


class AmazonMobileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Mobile.objects.all()
    serializer_class = serializers.AmazonMobileSerializer


class AmazonBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.AmazonBrandSerializer


class AmazonVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.AmazonVendorSerializer
