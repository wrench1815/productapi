from rest_framework import serializers

from .models import Product, Category, Vendor, Brand


class FlipkartProductSerializer(serializers.ModelSerializer):
    '''Serializer for Flipkart Product Model'''

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class FlipkartBrandSerializer(serializers.ModelSerializer):
    '''Serializer for Flipkart Product Model'''

    class Meta:
        model = Brand
        fields = '__all__'
        depth = 1


class FlipkartCategorySerializer(serializers.ModelSerializer):
    '''Serializer for Flipkart Product Model'''

    class Meta:
        model = Category
        fields = '__all__'
        depth = 1


class FlipkartVendorSerializer(serializers.ModelSerializer):
    '''Serializer for Flipkart Product Model'''

    class Meta:
        model = Vendor
        fields = '__all__'
        depth = 1
