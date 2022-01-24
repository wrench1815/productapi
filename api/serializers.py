from django.db.models import fields
from rest_framework import serializers
from flipkart.models import Product


class ProductSerializer(serializers.ModelSerializer):
    '''Serializer for Product Model'''

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1
