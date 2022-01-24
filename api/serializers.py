from rest_framework import serializers

# flipkart imports
from flipkart.models import Product as fproduct

# amazon imports
from amazon.models import Product as aproduct


class FlipkartProductSerializer(serializers.ModelSerializer):
    '''Serializer for Flipkart Product Model'''

    class Meta:
        model = fproduct
        fields = '__all__'
        depth = 1


class AmazonProductSerializer(serializers.ModelSerializer):
    '''Serializer for Amazon Product Model'''

    class Meta:
        model = aproduct
        fields = '__all__'
        depth = 1
