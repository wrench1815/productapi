from rest_framework import viewsets

from . import models
from . import serializers


class FlipkartMobileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Mobile.objects.all()
    serializer_class = serializers.FlipkartMobileSerializer


class FlipkartBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.FlipkartBrandSerializer


class FlipkartVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.FlipkartVendorSerializer
