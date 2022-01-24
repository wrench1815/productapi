from rest_framework import viewsets
from .serializers import FlipkartProductSerializer, AmazonProductSerializer

# flipkart imports
from flipkart.models import Product as fproduct

# amazon imports
from amazon.models import Product as aproduct


class FlipkartProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = fproduct.objects.all()
    serializer_class = FlipkartProductSerializer


class AmazonProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = aproduct.objects.all()
    serializer_class = AmazonProductSerializer
