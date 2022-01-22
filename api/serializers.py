from django.db.models import fields
from rest_framework import serializers
from flipkart.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
