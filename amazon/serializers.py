from rest_framework import serializers

from .models import Product, Category, Vendor, Brand


class AmazonProductSerializer(serializers.ModelSerializer):
    '''Serializer for Amazon Product Model'''

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class AmazonBrandSerializer(serializers.ModelSerializer):
    '''Serializer for Amazon Product Model'''

    class Meta:
        model = Brand
        fields = '__all__'
        depth = 1


class AmazonCategorySerializer(serializers.ModelSerializer):
    '''Serializer for Amazon Product Model'''

    class Meta:
        model = Category
        fields = '__all__'
        depth = 1


class AmazonVendorSerializer(serializers.ModelSerializer):
    '''Serializer for Amazon Product Model'''

    class Meta:
        model = Vendor
        fields = '__all__'
        depth = 1
