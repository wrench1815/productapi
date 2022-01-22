from rest_framework import viewsets
from .serializers import ProductSerializer as fProductSerializer
from flipkart.models import Product as fproduct


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = fproduct.objects.all()
    serializer_class = fProductSerializer
