from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import ProductDetail


class ProductDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(required=True,
                                         min_length=3)
    product_desc = serializers.CharField(required=False)
    mrp = serializers.IntegerField(required=True)

    class Meta:
        model = ProductDetail
        fields = ('product_name', 'product_desc', 'mrp')


