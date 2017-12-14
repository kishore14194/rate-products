from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from orders.models import OrdersCart
from .models import ProductDetail, ProductRating


class ProductDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(required=True,
                                         min_length=3, trim_whitespace=True)
    product_desc = serializers.CharField(required=False)
    mrp = serializers.IntegerField(required=True)

    class Meta:
        model = ProductDetail
        fields = ('product_name', 'product_desc', 'mrp')


class ProductRatingSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(required=True, min_length=3)
    comments = serializers.CharField(required=False, trim_whitespace=True)
    rating = serializers.IntegerField(required=True, max_value=5, min_value=0)

    class Meta:
        model = ProductRating
        fields = ('product_id', 'rating', 'comments')
