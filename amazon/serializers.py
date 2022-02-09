from rest_framework import serializers

from . import models


class AmazonMobileSerializer(serializers.ModelSerializer):
    '''Serializer for Amazon Mobile Model'''

    class Meta:
        model = models.Mobile
        fields = '__all__'
        depth = 2


class AmazonBrandSerializer(serializers.ModelSerializer):
    '''Serializer for Amazon Brand Model'''

    class Meta:
        model = models.Brand
        fields = '__all__'
        depth = 1


class AmazonVendorSerializer(serializers.ModelSerializer):
    '''Serializer for Amazon Vendor Model'''

    class Meta:
        model = models.Vendor
        fields = '__all__'
        depth = 1
