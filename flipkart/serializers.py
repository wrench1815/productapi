from rest_framework import serializers

from . import models


class FlipkartMobileSerializer(serializers.ModelSerializer):
    '''Serializer for Flipkart Mobile Model'''

    class Meta:
        model = models.Mobile
        fields = '__all__'
        depth = 2


class FlipkartBrandSerializer(serializers.ModelSerializer):
    '''Serializer for Flipkart Brand Model'''

    class Meta:
        model = models.Brand
        fields = '__all__'
        depth = 1


class FlipkartVendorSerializer(serializers.ModelSerializer):
    '''Serializer for Flipkart Vendor Model'''

    class Meta:
        model = models.Vendor
        fields = '__all__'
        depth = 1
